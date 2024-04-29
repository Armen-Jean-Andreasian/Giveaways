# Parsing

## Info

- Steam API: has no protection. To see max amount requests, check Steam API docs
- Steam website: has no protection. Any amount of requests
- Epic Games website: has Cloudflare anti-bot protection (not anti-scrap)
- Gog website: has no protection. Any amount of requests

---

# Content (we hunt for)

Content is the data needed to scrap, it could be txt/img/video, etc

The abstraction:

- `Content`
    - `ScrapableContent` (content obtained via scraping)
    - RequestableContent (content obtained from API)

### Containing

- `Content` abstraction level has:
    - `_analyze_response` abstract method
    - `content` abstract property.

- `ScrapableContent` has :
    - `url`: class attribute
    - `headers`: class attribute
    - `cookies`: class attribute
    - `params`: class attribute
    - `xpath`: class attribute
    - `css_selector`: class attribute
    - `html_structure`: class attribute
    - `__init__` : as an abstract method

- `RequestableContent` has :
    - `api_url`: class attribute
    - `headers`: class attribute
    - `cookies`: class attribute
    - `params`: class attribute
    - `__init__` : as an abstract method

Notes:

Adding `__init__` as an abstract method:

1. Allows to keep track of the structure and keep the code consistent
2. Increases encapsulation
3. Removes the need of invoking the overridden `__init__` method by using the `super()` and only negative effects of it.
    - calling the parent method which is additional logic
    - instance attribute doesn't visually exist on the instance level.
    - literally no reason to do that
    - the most important, OOP should flow from top to bottom, not reversed.

# Models

---

## App response

A simple interface to gather all given kwargs in a dictionary.

```python
from typing import Hashable, Any


def prototype(**kwargs) -> dict[Hashable, Any]:
    _result = {}
    given_kwargs = locals()['kwargs']

    for kwarg_key, kwarg_val in given_kwargs.items():
        _result[kwarg_key] = kwarg_val

    return _result
```

---

## Html Structure (not implemented)

### A Data Model for recreating the HTML hierarchy to the element.

For example, we have HTML code and our task is to get the image,

```HTML

<div class="logo">
    <a href="https://www.google.com/webhp?hl=en&amp;sa=X&amp;ved=0ahUKEwi6iYWyrOSFAxVGsVYBHZlTD7wQPAgJ"
       title="Go to Google Home"
       id="logo"
       data-hveid="9">

        <img class="jfN4p"
             src="/images/branding/googlelogo/2x/googlelogo_light_color_92x30dp.png"
             style="background:none"
             alt="Google"
             height="30"
             width="92"
             data-csiid="5"
             data-atf="1">
    </a>
</div>
```

1. First we need to access the tag `class` where the value is 'logo'.
2. Then find the tag `img`, and extract the link to image.

This model allows to save the chain of tags together.

### Usage:

- Initialize the class
- add `tag:value` pairs calling add_tag_val method, which will store them in the `self.container` list as a
  dictionary, following the pattern `{'tag': tag, 'value': value}`.
- In this way you have a list of dictionaries left to right representing HTML code depth from top to bottom
- get the container using `structure` getter, which will also clear `self.container`

In this example:

```python
from src.models import HtmlStructure

html_tag_structure = HtmlStructure()
html_tag_structure.add_tag_val(tag='class', value='logo')
html_tag_structure.add_tag_val(tag='img')

print(html_tag_structure.structure)
```

And the output will be:

```
[{'tag': 'class', 'value': 'logo'}, {'tag': 'img', 'value': None}]
```

### Trade-off

This will allow to iterate over `html_tag_structure.structure` using an analyzer (like `bs4`) and access the data.
