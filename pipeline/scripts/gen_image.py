#!/usr/bin/env python3
"""gen_image.py - image generation adapters for the Gemini API and the OpenAI Images API.

*** UNTESTED AGAINST LIVE APIs. ***  No API key has been supplied to this project and no
network call has ever been made by this file. Request shapes, endpoint paths, parameter
names and response fields below are written from recollection of the providers' public
documentation and from search-summary level reading on 2026-10-12 (no primary documentation
page could be opened). Expect to fix them on the first real run. Model names are NOT
defaulted: pass --model (or set GEMINI_IMAGE_MODEL / OPENAI_IMAGE_MODEL) with the exact id
from the provider's current model page, because ids and deprecations change often.

Standard library only.

INERT BY DEFAULT
  * No network call is made unless the provider's key variable is set in the environment
    (GEMINI_API_KEY or OPENAI_API_KEY) AND --dry-run is not given.
  * --dry-run prints the exact request (key masked) and the provenance row that would be
    written, then exits. It needs no key.
  * The key is read only from the environment. It is never accepted on the command line,
    never printed, never written to the provenance row, and is scrubbed from error text.

SAFETY RULES (BRIEF ground rules 2 and 3; pipeline/image-pack/README-photoreal.md section 5)
  * Prompts that name a real person, a celebrity or an existing character/virtual influencer
    are REFUSED by a simple keyword blocklist. The blocklist is a seatbelt, not clearance: a
    prompt that passes can still describe a real person. The look-alike checks (reverse-image
    search, the wife's check, the blind test) are still required on every face.
  * --reference images must live under assets/<persona>/ (that character's own generated
    images only). Anything else, and anything under a 'lookalike' folder (screenshots of
    search results that may show real people), is REFUSED.
  * The output path must also be under assets/<persona>/ and must not already exist: masters
    are never overwritten.
  * Image bytes are written exactly as received. Nothing is re-encoded or stripped, so any
    provider watermark or metadata (C2PA, SynthID) stays in the file.
  * A daily call cap (default 40, env GEN_IMAGE_MAX_PER_DAY) counts today's rows written by this script
    in assets/provenance.csv and refuses to send more. It limits a runaway loop; it is NOT a billing cap,
    so set a hard monthly budget in the provider's own console as well.
  * After a successful write, a row is appended to assets/provenance.csv via provenance.py.
    The row is validated BEFORE the API is called, so a spend is never followed by a refused log.

Exit codes: 0 ok / dry-run; 2 bad arguments; 3 inert (no key); 4 refused by a safety rule;
5 provider or network failure; 6 image written but provenance row failed (log it by hand).
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import mimetypes
import os
import re
import sys
import uuid
from dataclasses import dataclass, field
from pathlib import Path

import provenance

ROOT = Path(__file__).resolve().parents[2]

EXIT_OK, EXIT_ARGS, EXIT_INERT, EXIT_REFUSED, EXIT_API, EXIT_PROV = 0, 2, 3, 4, 5, 6

PROVIDERS = {
    "gemini": {
        "key_env": "GEMINI_API_KEY",
        "model_env": "GEMINI_IMAGE_MODEL",
        "tool_label": "Gemini API (generateContent, image output)",
    },
    "openai": {
        "key_env": "OPENAI_API_KEY",
        "model_env": "OPENAI_IMAGE_MODEL",
        "tool_label": "OpenAI Images API",
    },
}

PHOTOREAL_PERSONAS = {"fangcun", "buzhou", "sehuan"}  # DECISIONS.md 2026-10-11/12: pilots are photoreal
MAX_REFERENCES = 3  # addendum: R01 plus at most two other golden images
DEFAULT_MAX_PER_DAY = 40  # assumption: a pilot's golden-set day is about 8 candidates x 4 prompts
WRITER_MARK = "written by pipeline/scripts/gen_image.py"
MAX_REF_BYTES = 20 * 1024 * 1024
IMAGE_EXTS = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".webp": "image/webp"}

GEMINI_ASPECTS = ["1:1", "2:3", "3:2", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9", "21:9"]
# OpenAI gpt-image sizes as recalled (UNVERIFIED): 1024x1024, 1024x1536, 1536x1024, auto.
OPENAI_SIZE_FOR_ASPECT = {
    "1:1": "1024x1024",
    "4:5": "1024x1536", "2:3": "1024x1536", "3:4": "1024x1536", "9:16": "1024x1536",
    "16:9": "1536x1024", "3:2": "1536x1024", "4:3": "1536x1024", "5:4": "1536x1024", "21:9": "1536x1024",
}
OPENAI_EXACT_ASPECTS = {"1:1", "2:3", "3:2"}

REMINDER = (
    "Reminder: the blocklist is a keyword check, not clearance. A prompt that passes can still "
    "describe a real person. Never name or upload a real person; run the look-alike checks on "
    "every face (README-photoreal.md section 5 and the pack's reverse-image procedure)."
)

# --------------------------------------------------------------------------- prompt blocklist

# Real people (a small seed, NOT exhaustive) and existing characters / virtual influencers /
# franchises. Naming any of them in a prompt is refused even inside a prohibition ("not X"),
# because the project rule is that prompts name nobody. Extend via pipeline/scripts/blocklist_extra.txt.
BLOCK_NAMES_EN = [
    # real people (celebrities, politicians), seed list
    "taylor swift", "beyonce", "rihanna", "zendaya", "scarlett johansson", "emma watson",
    "angelina jolie", "jennifer lawrence", "margot robbie", "kim kardashian", "kylie jenner",
    "elon musk", "donald trump", "joe biden", "barack obama", "xi jinping", "tsai ing-wen",
    "lai ching-te", "ko wen-je", "han kuo-yu", "hou yu-ih", "jay chou", "jolin tsai",
    "lin chi-ling", "shu qi", "blackpink", "newjeans",
    # existing characters, virtual influencers, franchises and studios
    "hello kitty", "pikachu", "mickey mouse", "minnie mouse", "doraemon", "totoro", "naruto",
    "goku", "sailor moon", "elsa", "spider-man", "spiderman", "batman", "superman", "wonder woman",
    "harry potter", "hatsune miku", "lil miquela", "miquela", "imma", "kizuna ai", "mia zelu",
    "noonoouri", "shudu", "barbie", "lego", "minecraft", "studio ghibli", "ghibli", "disney",
    "pixar", "marvel", "line friends",
]
BLOCK_NAMES_ZH = [
    "周杰倫", "蔡依林", "林志玲", "舒淇", "桂綸鎂", "楊丞琳", "田馥甄", "林依晨", "周子瑜", "蔡英文",
    "賴清德", "柯文哲", "韓國瑜", "侯友宜", "習近平", "郭台銘", "館長", "蔡康永",
    "初音未來", "皮卡丘", "哆啦A夢", "多啦A夢", "蠟筆小新", "角落小夥伴", "凱蒂貓", "米老鼠", "吉卜力",
    "迪士尼", "皮克斯", "樂高", "虎妮", "宮祈緣", "OPEN將",
]
# Likeness phrases followed by a Capitalised name are refused (looks like Zendaya, in the style of Hayao...).
_LIKENESS_NAME_RE = re.compile(
    r"(?i:\b(?:looks?\s+like|looking\s+like|resembl(?:e|es|ing)|similar\s+to|modell?ed\s+(?:on|after)|"
    r"based\s+on|inspired\s+by|in\s+the\s+style\s+of|lookalike\s+of|look-alike\s+of|likeness\s+of)\s+(?:the\s+|a\s+|an\s+)?)"
    r"(?P<name>[A-Z][\w'’.\-]+)"
)
_STYLE_OF_RE = re.compile(r"(?i)\bin\s+the\s+style\s+of\b")
_LIKENESS_ZH_RE = re.compile(r"(長得像|看起來像|看來像|神似|酷似|仿照|仿造|參考照片|根據照片|以.{1,6}為原型|以.{1,6}為藍本)")
_ZH_NEGATORS = ("不要", "不可", "不能", "避免", "請勿", "勿", "別", "無", "不")
_GENERIC_RISK_WORDS = [
    "celebrity", "celebrities", "famous", "idol", "supermodel", "influencer", "actress", "actor",
    "singer", "politician", "k-pop", "kpop", "news anchor", "anchorwoman",
]
_EN_NEGATION_RE = re.compile(r"\b(?:not|no|never|avoid|without|nor|neither|don't|do not|must not|any resemblance)\b", re.I)
_BRAND_WARN = ["ikea", "muji", "無印良品", "uniqlo", "nike", "adidas", "apple", "iphone", "starbucks",
               "7-eleven", "familymart", "全家", "shopee", "蝦皮"]
_HEX_RE = re.compile(r"#[0-9A-Fa-f]{6}\b")
_TEXT_REQUEST_RE = re.compile(r"(?i)\b(?:text|caption|words|sign|label|logo|slogan)\s+(?:saying|reading|that says|which says)\b")
_CJK_RE = re.compile(r"[\u3400-\u9fff]")


@dataclass
class PromptCheck:
    blocked: list = field(default_factory=list)
    warnings: list = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.blocked


def load_extra_blocklist(path: Path | None = None) -> list[str]:
    path = path or Path(__file__).with_name("blocklist_extra.txt")
    if not path.exists():
        return []
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            out.append(line)
    return out


def _sentence_before(text: str, idx: int) -> str:
    cut = max(text.rfind(c, 0, idx) for c in ".\n!?")
    return text[cut + 1: idx]


def check_prompt(prompt: str, extra_terms=()) -> PromptCheck:
    res = PromptCheck()
    low = prompt.lower()
    for term in list(BLOCK_NAMES_EN) + [t for t in extra_terms if t.isascii()]:
        if re.search(r"(?<![a-z0-9])" + re.escape(term.lower()) + r"(?![a-z0-9])", low):
            res.blocked.append(f"names a real person or existing character/franchise: '{term}'")
    for term in list(BLOCK_NAMES_ZH) + [t for t in extra_terms if not t.isascii()]:
        if term in prompt:
            res.blocked.append(f"names a real person or existing character/franchise: '{term}'")
    for m in _LIKENESS_NAME_RE.finditer(prompt):
        res.blocked.append(f"likeness phrase followed by a name: '{m.group(0).strip()}' (never use 'looks like' / 'in the style of' + a name)")
    for m in _STYLE_OF_RE.finditer(prompt):
        if not _LIKENESS_NAME_RE.search(prompt[m.start(): m.end() + 40]):
            res.warnings.append("'in the style of' found: never follow it with a living artist, studio or character")
    for m in _LIKENESS_ZH_RE.finditer(prompt):
        before = prompt[max(0, m.start() - 6): m.start()]
        if any(n in before for n in _ZH_NEGATORS):
            continue
        res.blocked.append(f"Chinese likeness phrase: '{m.group(0)}'")
    for w in _GENERIC_RISK_WORDS:
        for m in re.finditer(r"(?<![a-z])" + re.escape(w) + r"(?![a-z])", low):
            if not _EN_NEGATION_RE.search(_sentence_before(low, m.start())):
                res.warnings.append(f"generic risk word '{w}' used affirmatively: a character must be original, not 'a celebrity/idol/model'")
                break
    for b in _BRAND_WARN:
        if b.isascii():
            hit = re.search(r"(?<![a-z0-9])" + re.escape(b) + r"(?![a-z0-9])", low)
        else:
            hit = b in prompt
        if hit:
            res.warnings.append(f"real brand named: '{b}' (no real brands or logos in prompts)")
    if _HEX_RE.search(prompt):
        res.warnings.append("hex colour code in prompt: a generator can print it into the picture; name colours in words")
    if _TEXT_REQUEST_RE.search(prompt):
        res.warnings.append("prompt asks for text in the picture: generators garble or Simplify Chinese; add text in post instead")
    elif _CJK_RE.search(prompt):
        res.warnings.append("Chinese characters in an image prompt: they may be printed into the picture; add Chinese text in post")
    # de-duplicate, keep order
    res.blocked = list(dict.fromkeys(res.blocked))
    res.warnings = list(dict.fromkeys(res.warnings))
    return res


# --------------------------------------------------------------------------- path rules

class RefusedError(Exception):
    pass


def _persona_dir(root: Path, persona: str) -> Path:
    return (root / "assets" / persona).resolve()


def check_reference(path_str: str, persona: str, root: Path) -> Path:
    """Return the resolved reference path or raise RefusedError.

    Relative paths are resolved against the project folder. The resolved real path
    (symlinks followed) must lie under assets/<persona>/."""
    p = Path(path_str)
    if not p.is_absolute():
        p = root / p
    try:
        real = p.resolve(strict=True)
    except (FileNotFoundError, OSError):
        raise RefusedError(f"reference image not found: {path_str}")
    base = _persona_dir(root, persona)
    try:
        rel = real.relative_to(base)
    except ValueError:
        raise RefusedError(
            f"reference image {path_str!r} is not under assets/{persona}/. Only that character's own "
            "generated images may be uploaded as references (never a photo of a real person, never another "
            "persona's image, never a screenshot or fan art).")
    if any(part.lower() == "lookalike" for part in rel.parts):
        raise RefusedError("references from a 'lookalike' folder are refused: those screenshots can show real people")
    if not real.is_file():
        raise RefusedError(f"reference is not a file: {path_str}")
    if real.suffix.lower() not in IMAGE_EXTS:
        raise RefusedError(f"reference must be one of {', '.join(IMAGE_EXTS)}: {path_str}")
    if real.stat().st_size > MAX_REF_BYTES:
        raise RefusedError(f"reference larger than {MAX_REF_BYTES // (1024 * 1024)} MB: {path_str}")
    return real


def check_output_path(path_str: str, persona: str, root: Path) -> Path:
    p = Path(path_str)
    if not p.is_absolute():
        p = root / p
    real = p.resolve(strict=False)
    base = _persona_dir(root, persona)
    try:
        real.relative_to(base)
    except ValueError:
        raise RefusedError(f"output path must be under assets/{persona}/: {path_str}")
    if real.suffix.lower() not in IMAGE_EXTS:
        raise RefusedError(f"output file name must end in one of {', '.join(IMAGE_EXTS)}: {path_str}")
    if real.exists():
        raise RefusedError(f"output file already exists and will not be overwritten (masters are never overwritten): {path_str}")
    return real


def sniff_ext(data: bytes) -> str | None:
    if data.startswith(b"\x89PNG\r\n\x1a\n"):
        return ".png"
    if data.startswith(b"\xff\xd8\xff"):
        return ".jpg"
    if data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        return ".webp"
    return None


# --------------------------------------------------------------------------- requests

@dataclass
class Request:
    provider: str
    method: str
    url: str
    auth_header: str          # header name that carries the key
    auth_scheme: str          # '' or 'Bearer '
    json_body: dict | None = None
    form_fields: dict | None = None
    form_files: list | None = None   # list of (field_name, filename, mime, bytes)
    note: str = ""

    def body_and_type(self):
        if self.json_body is not None:
            return json.dumps(self.json_body).encode("utf-8"), "application/json"
        return encode_multipart(self.form_fields or {}, self.form_files or [])

    def display(self) -> str:
        """Human-readable view with the key masked and base64 data truncated. Never contains a secret."""
        lines = [f"{self.method} {self.url}", f"  header {self.auth_header}: {self.auth_scheme}***(from env, not printed)"]
        if self.json_body is not None:
            lines.append("  Content-Type: application/json")
            lines.append("  body:")
            lines.append(_indent(json.dumps(_truncate_b64(self.json_body), indent=2, ensure_ascii=False), 4))
        else:
            lines.append("  Content-Type: multipart/form-data")
            lines.append("  fields:")
            lines.append(_indent(json.dumps(self.form_fields, indent=2, ensure_ascii=False), 4))
            for name, fn, mime, data in (self.form_files or []):
                lines.append(f"  file {name}: {fn} ({mime}, {len(data)} bytes)")
        if self.note:
            lines.append("  note: " + self.note)
        return "\n".join(lines)


def _indent(s: str, n: int) -> str:
    pad = " " * n
    return "\n".join(pad + ln for ln in s.splitlines())


def _truncate_b64(obj):
    if isinstance(obj, dict):
        return {k: (f"<base64, {len(v)} chars>" if k == "data" and isinstance(v, str) and len(v) > 80 else _truncate_b64(v))
                for k, v in obj.items()}
    if isinstance(obj, list):
        return [_truncate_b64(x) for x in obj]
    return obj


def encode_multipart(fields: dict, files: list):
    boundary = "----pipeline" + uuid.uuid4().hex
    out = bytearray()
    for k, v in fields.items():
        out += f"--{boundary}\r\nContent-Disposition: form-data; name=\"{k}\"\r\n\r\n{v}\r\n".encode("utf-8")
    for name, filename, mime, data in files:
        out += (f"--{boundary}\r\nContent-Disposition: form-data; name=\"{name}\"; filename=\"{filename}\"\r\n"
                f"Content-Type: {mime}\r\n\r\n").encode("utf-8")
        out += data + b"\r\n"
    out += f"--{boundary}--\r\n".encode("utf-8")
    return bytes(out), f"multipart/form-data; boundary={boundary}"


def build_gemini_request(prompt: str, model: str, refs: list[Path], aspect_ratio: str, image_size: str | None) -> Request:
    parts = [{"text": prompt}]
    for r in refs:
        parts.append({"inline_data": {"mime_type": IMAGE_EXTS[r.suffix.lower()],
                                      "data": base64.b64encode(r.read_bytes()).decode("ascii")}})
    image_cfg = {"aspectRatio": aspect_ratio}
    if image_size:
        image_cfg["imageSize"] = image_size
    body = {
        "contents": [{"role": "user", "parts": parts}],
        "generationConfig": {"responseModalities": ["TEXT", "IMAGE"], "imageConfig": image_cfg},
    }
    return Request(
        provider="gemini", method="POST",
        url=f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent",
        auth_header="x-goog-api-key", auth_scheme="", json_body=body,
        note="UNTESTED shape. imageConfig.imageSize and responseModalities support varies by model (unverified).",
    )


def build_openai_request(prompt: str, model: str, refs: list[Path], aspect_ratio: str, size: str | None,
                         quality: str, output_format: str) -> Request:
    derived = size is None
    size = size or OPENAI_SIZE_FOR_ASPECT.get(aspect_ratio, "1024x1536")
    note = "UNTESTED shape."
    if derived and aspect_ratio not in OPENAI_EXACT_ASPECTS:
        note += (f" Aspect {aspect_ratio} is not offered natively; size {size} is the nearest recalled option (unverified). "
                 "Crop in post and log the crop as a human edit.")
    if refs:
        fields = {"model": model, "prompt": prompt, "size": size, "quality": quality,
                  "n": "1", "output_format": output_format}
        files = [("image[]", r.name, IMAGE_EXTS[r.suffix.lower()], r.read_bytes()) for r in refs]
        return Request(provider="openai", method="POST", url="https://api.openai.com/v1/images/edits",
                       auth_header="Authorization", auth_scheme="Bearer ", form_fields=fields, form_files=files,
                       note=note + " References are sent to the edits endpoint as image[] (unverified).")
    body = {"model": model, "prompt": prompt, "size": size, "quality": quality, "n": 1, "output_format": output_format}
    return Request(provider="openai", method="POST", url="https://api.openai.com/v1/images/generations",
                   auth_header="Authorization", auth_scheme="Bearer ", json_body=body, note=note)


# --------------------------------------------------------------------------- transport

class ApiError(Exception):
    pass


def redact(text: str, *secrets: str) -> str:
    for s in secrets:
        if s:
            text = text.replace(s, "***")
    for rx in provenance._SECRET_RES:
        text = rx.sub("***", text)
    return text


def http_post(url: str, headers: dict, data: bytes, timeout: float = 180.0):
    """The ONLY function in this project that opens a network connection. Returns (status, body bytes)."""
    import urllib.error
    import urllib.request
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read()
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        raise ApiError(f"network failure: {type(e).__name__}")


def parse_gemini_response(body: bytes):
    """Return (image_bytes, mime). Raises ApiError with a readable reason."""
    try:
        doc = json.loads(body.decode("utf-8"))
    except (ValueError, UnicodeDecodeError):
        raise ApiError("response was not JSON")
    fb = doc.get("promptFeedback") or {}
    if fb.get("blockReason"):
        raise ApiError(f"provider blocked the prompt: {fb.get('blockReason')}. Do not reword the prompt to get around a refusal; log it and tell Claude.")
    texts = []
    for cand in doc.get("candidates") or []:
        content = cand.get("content") or {}
        for part in content.get("parts") or []:
            inline = part.get("inlineData") or part.get("inline_data")
            if inline and inline.get("data"):
                mime = inline.get("mimeType") or inline.get("mime_type") or "image/png"
                return base64.b64decode(inline["data"]), mime
            if part.get("text"):
                texts.append(part["text"])
        fr = cand.get("finishReason")
        if fr and fr not in ("STOP", "MAX_TOKENS"):
            raise ApiError(f"no image; finishReason={fr}. Do not reword the prompt to get around a refusal; log it and tell Claude.")
    snippet = (" Model said: " + " ".join(texts)[:200]) if texts else ""
    raise ApiError("response contained no image part." + snippet)


def parse_openai_response(body: bytes):
    try:
        doc = json.loads(body.decode("utf-8"))
    except (ValueError, UnicodeDecodeError):
        raise ApiError("response was not JSON")
    if "error" in doc:
        err = doc["error"]
        msg = err.get("message") if isinstance(err, dict) else str(err)
        raise ApiError(f"provider error: {str(msg)[:300]}")
    data = doc.get("data") or []
    if data and data[0].get("b64_json"):
        return base64.b64decode(data[0]["b64_json"]), None
    if data and data[0].get("url"):
        raise ApiError("provider returned a URL instead of image data; this script makes no second network call")
    raise ApiError("response contained no image data")


# --------------------------------------------------------------------------- provenance

def build_provenance_row(*, provider: str, persona: str, asset_rel: str, model: str, prompt: str,
                         refs_rel: list[str], extra_note: str, timestamp: str) -> dict:
    prefix = "PHOTOREAL v2; " if persona in PHOTOREAL_PERSONAS else ""
    notes = (
        f"{prefix}Status: UNREVIEWED (raw API output, not yet through the QA checklist); reason: n/a; "
        f"parent file: none (raw download); reference images attached: {', '.join(refs_rel) if refs_rel else 'none'}; "
        "human edits: none (raw); prompt ID: n/a; tool plan: API account (plan not recorded by the script; the human adds it); "
        "terms read on: not yet read; commercial use per those terms: NOT CONFIRMED (internal design material only); "
        "visible mark or label on file or in the app: NOT INSPECTED (a provider watermark or metadata may be present, "
        "for example SynthID or C2PA; unverified; do not strip); conversation link or ID: none (API call); seed: none shown; "
        f"{WRITER_MARK} (UNTESTED adapter)"
    )
    if extra_note:
        notes += "; note: " + extra_note
    full_prompt = prompt
    if refs_rel:
        full_prompt += "\n[attached reference files: " + ", ".join(refs_rel) + "]"
    return {
        "timestamp": timestamp,
        "asset_path": asset_rel,
        "persona": persona,
        "tool": PROVIDERS[provider]["tool_label"],
        "model": model,
        "prompt": full_prompt,
        "licence_notes": notes,
    }


def calls_today(root: Path, day: str) -> int:
    """Rows in provenance.csv written by this script whose timestamp starts with `day` (YYYY-MM-DD)."""
    import csv
    path = root / provenance.CSV_RELPATH
    if not path.exists():
        return 0
    n = 0
    with open(path, newline="", encoding="utf-8") as fh:
        for rec in csv.DictReader(fh):
            if (rec.get("timestamp") or "").startswith(day) and WRITER_MARK in (rec.get("licence_notes") or ""):
                n += 1
    return n


# --------------------------------------------------------------------------- main flow

def _parser():
    ap = argparse.ArgumentParser(
        description="Generate one image with the Gemini API or OpenAI Images API (UNTESTED, inert without a key).",
        epilog="Set the key in the environment (GEMINI_API_KEY or OPENAI_API_KEY). Never paste a key into chat or a file.")
    ap.add_argument("--provider", required=True, choices=sorted(PROVIDERS))
    ap.add_argument("--persona", required=True, help="character slug, for example fangcun")
    ap.add_argument("--out", required=True, help="output image path, under assets/<persona>/, must not exist")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--prompt")
    g.add_argument("--prompt-file", type=Path)
    ap.add_argument("--model", help="exact model id from the provider's current model page (no default on purpose)")
    ap.add_argument("--reference", action="append", default=[], metavar="PATH",
                    help=f"reference image under assets/<persona>/ (repeatable, at most {MAX_REFERENCES})")
    ap.add_argument("--aspect-ratio", default="4:5", choices=GEMINI_ASPECTS)
    ap.add_argument("--image-size", help="Gemini only, for example 1K or 2K (model support unverified)")
    ap.add_argument("--size", help="OpenAI only, overrides the size derived from --aspect-ratio")
    ap.add_argument("--quality", default="medium", choices=["low", "medium", "high", "auto"], help="OpenAI only")
    ap.add_argument("--output-format", default="png", choices=["png", "jpeg", "webp"], help="OpenAI only")
    ap.add_argument("--note", default="", help="extra text appended to licence_notes")
    ap.add_argument("--dry-run", action="store_true", help="print the request and provenance row, send nothing, need no key")
    ap.add_argument("--root", type=Path, default=ROOT, help=argparse.SUPPRESS)
    ap.add_argument("--timestamp", help=argparse.SUPPRESS)
    return ap


def run(argv=None, *, env=None, post=http_post, out=print, err=None) -> int:
    err = err or (lambda s: print(s, file=sys.stderr))
    env = os.environ if env is None else env
    args = _parser().parse_args(argv)
    root = args.root.resolve()
    prov = PROVIDERS[args.provider]
    key = (env.get(prov["key_env"]) or "").strip()
    persona = args.persona

    try:
        prompt = args.prompt if args.prompt is not None else args.prompt_file.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as e:
        err(f"cannot read prompt file as UTF-8 text: {getattr(e, 'strerror', None) or type(e).__name__}")
        return EXIT_ARGS
    prompt = prompt.strip()
    if not prompt:
        err("prompt is empty")
        return EXIT_ARGS
    slugs = provenance.known_personas(root)
    if slugs is not None and persona not in slugs - {"studio"}:
        err(f"unknown persona {persona!r}; known: {', '.join(sorted(slugs - {'studio'}))}")
        return EXIT_ARGS
    if len(args.reference) > MAX_REFERENCES:
        err(f"at most {MAX_REFERENCES} reference images")
        return EXIT_ARGS

    # 1. safety rules (all before any spend)
    pc = check_prompt(prompt, load_extra_blocklist())
    if not pc.ok:
        err("REFUSED: the prompt breaks the likeness rule (Ground rule 2):")
        for b in pc.blocked:
            err("  - " + b)
        err(REMINDER)
        return EXIT_REFUSED
    try:
        refs = [check_reference(r, persona, root) for r in args.reference]
        out_path = check_output_path(args.out, persona, root)
    except RefusedError as e:
        err("REFUSED: " + str(e))
        return EXIT_REFUSED
    for w in pc.warnings:
        out("WARNING: " + w)

    # 2. request
    model = args.model or env.get(prov["model_env"], "").strip()
    if not model:
        if not args.dry_run:
            err(f"no model: pass --model or set {prov['model_env']} (no default on purpose; copy the id from the provider's current model page)")
            return EXIT_ARGS
        model = "<MODEL-NOT-SET>"
        out(f"WARNING: model not set (pass --model or set {prov['model_env']}); showing a placeholder")
    if args.provider == "gemini":
        req = build_gemini_request(prompt, model, refs, args.aspect_ratio, args.image_size)
    else:
        req = build_openai_request(prompt, model, refs, args.aspect_ratio, args.size, args.quality, args.output_format)

    # 3. provenance row, validated before any spend
    ts = args.timestamp or provenance.taiwan_now()
    try:
        asset_rel = out_path.relative_to(root.resolve()).as_posix()
    except ValueError:
        asset_rel = out_path.as_posix()
    refs_rel = [r.relative_to(root.resolve()).as_posix() for r in refs]
    row = build_provenance_row(provider=args.provider, persona=persona, asset_rel=asset_rel, model=model,
                               prompt=prompt, refs_rel=refs_rel, extra_note=args.note, timestamp=ts)
    problems = provenance.validate_row(row, root, check_exists=False)
    if problems:
        err("REFUSED: the provenance row would be invalid, so nothing was sent:")
        for p in problems:
            err("  - " + p)
        return EXIT_REFUSED

    if args.dry_run:
        out("DRY RUN: nothing sent, nothing written. UNTESTED request shape.\n")
        out(req.display())
        out("\nprovenance row that would be appended after a successful write:")
        for c in provenance.COLUMNS:
            out(f"  {c}: {row[c]}")
        out(f"\nkey variable {prov['key_env']}: {'set' if key else 'NOT set'} (value never printed)")
        out(REMINDER)
        return EXIT_OK

    # 4. inert unless the key is set
    if not key:
        err(f"INERT: {prov['key_env']} is not set, so no network call was made. Use --dry-run to inspect the request.")
        return EXIT_INERT

    # 5. daily cap, then send
    try:
        cap = int((env.get("GEN_IMAGE_MAX_PER_DAY") or DEFAULT_MAX_PER_DAY))
    except ValueError:
        cap = DEFAULT_MAX_PER_DAY
    done = calls_today(root, ts[:10])
    if done >= cap:
        err(f"REFUSED: {done} images were already generated today (cap {cap}, env GEN_IMAGE_MAX_PER_DAY). Nothing was sent.")
        return EXIT_REFUSED
    body, ctype = req.body_and_type()
    headers = {req.auth_header: req.auth_scheme + key, "Content-Type": ctype}
    try:
        status, resp_body = post(req.url, headers, body)
    except ApiError as e:
        err("API call failed: " + redact(str(e), key))
        return EXIT_API
    if status >= 400:
        snippet = redact(resp_body.decode("utf-8", "replace")[:300], key)
        err(f"API call failed: HTTP {status}: {snippet}")
        return EXIT_API
    try:
        if args.provider == "gemini":
            img, mime = parse_gemini_response(resp_body)
        else:
            img, mime = parse_openai_response(resp_body)
    except ApiError as e:
        err("API call failed: " + redact(str(e), key))
        return EXIT_API

    # 6. write exactly what was received, never overwrite
    sniffed = sniff_ext(img)
    if sniffed and sniffed != out_path.suffix.lower() and not (sniffed == ".jpg" and out_path.suffix.lower() == ".jpeg"):
        out(f"WARNING: file starts like {sniffed} but --out ends in {out_path.suffix}; written as received, rename by hand if needed (and log the rename).")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with open(out_path, "xb") as fh:
            fh.write(img)
    except FileExistsError:
        err("REFUSED: output file appeared while the request was running; image not written")
        return EXIT_REFUSED
    digest = hashlib.sha256(img).hexdigest()[:16]

    # 7. provenance
    try:
        provenance.append_row(row, root, check_exists=True)
    except provenance.ProvenanceError as e:
        err(f"IMAGE WRITTEN to {asset_rel} BUT THE PROVENANCE ROW FAILED: {e}. Log it by hand today (Ground rule 2).")
        return EXIT_PROV
    out(f"Wrote {asset_rel} ({len(img)} bytes, sha256 {digest}...) and appended a provenance row.")
    out("Next: QA checklist at 100% and 200%, hands first; the badge is added in post; the platform AI label is switched on by hand.")
    return EXIT_OK


if __name__ == "__main__":
    sys.exit(run())
