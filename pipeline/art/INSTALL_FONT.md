# Installing the Chinese font used for diagram text (Noto Sans TC)

Noto Sans TC (SIL Open Font License 1.1) is the font named in the bibles for any Chinese text added to images in post-production.

Install (done once in a session; fonts are not stored in git because the files are large):

```
mkdir -p /tmp/fontdl && cd /tmp/fontdl
npm pack @expo-google-fonts/noto-sans-tc      # contains NotoSansTC_*.ttf
mkdir x && tar xzf expo-google-fonts-noto-sans-tc-*.tgz -C x
mkdir -p ~/.fonts
cp x/package/400Regular/NotoSansTC_400Regular.ttf x/package/500Medium/NotoSansTC_500Medium.ttf x/package/700Bold/NotoSansTC_700Bold.ttf ~/.fonts/
fc-cache -f
fc-list | grep "Noto Sans TC"
```

Rendering must set `lang="zh-Hant-TW"` and `font-family: "Noto Sans TC"` so Taiwan glyph shapes are chosen. If the font is missing, the render falls back to another font: stop and install it, do not ship the fallback.
