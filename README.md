# GitHub Action to Purge Cloudflare Cache  🗑️ 


## Usage

All sensitive variables should be [set as encrypted secrets](https://help.github.com/en/articles/virtual-environments-for-github-actions#creating-and-using-secrets-encrypted-variables) in the action's configuration.

### `workflow.yml` Example

#### Run using CloudFlare auth token
```yaml
    - name: Purge cache
      uses: aorfanos/cloudflare-purge-action@main
      env:
        CF_TOKEN: ${{ secrets.CF_TOKEN }}
        CF_ZONE_NAME: ${{ secrets.CF_ZONE_NAME }}
```

#### Run using legacy CloudFlare API key
```yaml
    - name: Purge cache
      uses: aorfanos/cloudflare-purge-action@main
      env:
        CF_EMAIL_ADDR: ${{ secrets.CF_EMAIL_ADDR }}
        CF_API_KEY: ${{ secrets.CF_API_KEY }}
        CF_ZONE_NAME: ${{ secrets.CF_ZONE_NAME }}
```


### Purging specific files

To purge only specific files, you can pass an array of **fully qualified URLs** via a fourth environment variable named `CF_PURGE_URLS`.

```yaml
CF_PURGE_URLS: '["https://aorfanos.com/styles.css","https://aorfanos.com/style.css"]'
```
