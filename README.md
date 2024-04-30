# Game giveaways 

As a parser this provides simplicity and reliability.

As a piece of code this provides high readability and extendability. 

- Status: In development
- Platforms: Steam
- Features: 
  - Steam:
    - -100% discounted games
    - -100% discounted bundles 
    - -100% discounted DLC-s
    - Temporarily free to access games (aka Free Weekend)
  - Epic Games:
    - -100% discounted games
    - -100% discounted DLC-s

For more detailed information read [documentation.md](docs/documentation.md)

---
# Information

- Steam: gathered from SteamAPI, Steam Store (none of them frequently change the structure)

---
# Integration

The output follows REST principles, so it needs only iterating over the result:
Example from `demo.py`

```python
import streamlit as st
from src.app import App

deals = App.get_deals(steam_free_weekend=True, steam_giveaways=True)

for key, val in deals.items():
    if val:
        match key:
            case 'steam_giveaways':
                st.title("Steam Giveaways")
            case 'steam_free_weekend':
                st.title("Steam Free Weekend")
        st.divider()

        for dictionary in val:
            st.subheader(f"Game name: {dictionary['game_name']}")
            st.subheader(f"Game ID: {dictionary['game_id']}")
            st.image(dictionary['rectangle_img_url'])
            st.link_button(label="See", url=dictionary['game_url'])
```

Result:

![img.png](github%2Fimg.png)

*_No current 'free weekend' at this moment._

---

# Credits:

Armen-Jean Andreasian, 2024