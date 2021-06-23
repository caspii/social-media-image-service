# Social Media Image Service
This is a dockerized Python Flask application which renders a screenshot for a given URL. It is useful for automatically generating social 
media images for content which doesn't have its own social media image and is shared on services like Twitter, WhatsApp or Facebook.

Read this [article for the whole backstory](https://casparwre.de/blog/social-media-image-generation-python/).

Screenshots are rendered using the Firefox webdriver for Selenium.

## Deploying
The easiest way to deploy this is using Docker. The recommended RAM for the container is 4GB.

You must set an ENV variable defining the domain for which the images can be rendered for. To be able to render images for Wikipedia articles, for instance, do this

```
export DOMAIN=https://wikipedia.org
```

This is to prevent the deployed service from being misused. If you don't like it, fork and change it.

## Usage

For example, say you wanted to generate an image for `https://en.wikipedia.org/wiki/Ocelot`

1. Deploy the service to a publicly available URL, lets call it `<SERVICE-URL>`
1. URL encode the page you want to generate the image for. It will look something like this ```https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FOcelot```
3. Now you add a '.png' to the end of it and then call the following URL to get a rendered image of this page: `<SERVICE-URL>/image/https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FOcelot.png`
4. This is what you would add to your HTML:
```html
<meta property="og:image" content="<SERVICE-URL>/image/https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FOcelot.png" />
```

## Contribute
If you would like to add features, please get in touch first.
