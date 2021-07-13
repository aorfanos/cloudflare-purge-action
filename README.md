# GitHub Action to Purge Cloudflare Cache  🗑️ 

A fast GitHub action (python+composite run) to purge CloudFlare cache. 

## Usage

If you are running it from a custom container (e.g. not `ubuntu-latest` or similar provided by GitHub), this container needs to have python installed.

All sensitive variables should be [set as encrypted secrets](https://help.github.com/en/articles/virtual-environments-for-github-actions#creating-and-using-secrets-encrypted-variables) in the action's configuration.

### `workflow.yml` Example

#### Run using CloudFlare auth token
```yaml
    - name: Purge cache
      uses: aorfanos/cloudflare-purge-action@v1.0.3
      env:
        CF_TOKEN: ${{ secrets.CF_TOKEN }}
        CF_ZONE_NAME: ${{ secrets.CF_ZONE_NAME }}
```

#### Run using legacy CloudFlare API key
```yaml
    - name: Purge cache
      uses: aorfanos/cloudflare-purge-action@v1.0.3
      env:
        CF_EMAIL_ADDR: ${{ secrets.CF_EMAIL_ADDR }}
        CF_API_KEY: ${{ secrets.CF_API_KEY }}
        CF_ZONE_NAME: ${{ secrets.CF_ZONE_NAME }}
```

### Purge everything from a zone

Just specify authentication and zone name to purge everything. 

### Purging specific files

To purge only specific files, you can pass an array of **fully qualified URLs** via the environment variable named `CF_PURGE_URLS`.

[CF API Doc](https://api.cloudflare.com/#zone-purge-files-by-url)
```yaml
CF_PURGE_URLS: '["https://aorfanos.com/styles.css","https://aorfanos.com/style.css"]'
```

### Purge hosts

[CF API Doc](https://api.cloudflare.com/#zone-purge-files-by-cache-tags,-host-or-prefix)
```yaml
CF_PURGE_HOSTS: '["https://aorfanos.com","https://blog.aorfanos.com"]'
```

### Purge tags

[CF API Doc](https://api.cloudflare.com/#zone-purge-files-by-cache-tags,-host-or-prefix)
```yaml
CF_PURGE_TAGS: '["some-tag","another-tag"]'
```

### Purge by prefix

[CF API Doc](https://api.cloudflare.com/#zone-purge-files-by-cache-tags,-host-or-prefix)
```yaml
CF_PURGE_PREFIXES: '["https://aorfanos.com/css","https://aorfanos.com/js"]'
```