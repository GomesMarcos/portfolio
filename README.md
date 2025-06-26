
## Install TailWind
`$ curl -sLo static/css/tailwindcss https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-linux-x64`

`$ chmod +x static/css/tailwindcss`

`$ curl -sLo static/css/daisyui.js https://github.com/saadeghi/daisyui/releases/latest/download/daisyui.js`

`$ curl -sLo static/css/daisyui-theme.js https://github.com/saadeghi/daisyui/releases/latest/download/daisyui-theme.js`

### TailWind Commands
```
# Start a watcher
./static/css/tailwindcss -i static/css/input.css -o static/css/output.css --watch

# Compile and minify your CSS for production
./static/css/tailwindcss -i static/css/input.css -o static/css/output.css --minify
```

