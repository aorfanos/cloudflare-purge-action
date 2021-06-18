# GitHub Action to Purge Cloudflare Cache  🗑️ 


## Usage

All sensitive variables should be [set as encrypted secrets](https://help.github.com/en/articles/virtual-environments-for-github-actions#creating-and-using-secrets-encrypted-variables) in the action's configuration.


### `workflow.yml` Example

Place in a `.yml` file such as this one in your `.github/workflows` folder. [Refer to the documentation on workflow YAML syntax here.](https://help.github.com/en/articles/workflow-syntax-for-github-actions)

```yaml
name: Deploy my website
on: push

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:

    # Put steps here to build your site, deploy it to a service, etc.

    - name: Purge cache
      uses: aorfanos/cloudflare-purge-action@main
      inputs:
        # Zone is required by both authentication methods
        cf_zone_name: ${{ secrets.CLOUDFLARE_ZONE }}

        cf_token: ${{ secrets.CLOUDFLARE_TOKEN }}
        # ...or:
        cf_email_addr: ${{ secrets.CLOUDFLARE_EMAIL }}
        cf_api_key: ${{ secrets.CLOUDFLARE_KEY }}
```

### Purging specific files

To purge only specific files, you can pass an array of **fully qualified URLs** via a fourth environment variable named `PURGE_URLS`. Unfortunately, Cloudflare doesn't support wildcards (unless you're on the insanely expensive Enterprise plan) so in order to purge a folder, you'd need to list every file in that folder. It's probably safer to leave this out and purge everything, but in case you want really to, the syntax is as follows:

```yaml
PURGE_URLS: '["https://jarv.is/style.css", "https://jarv.is/favicon.ico"]'
```
