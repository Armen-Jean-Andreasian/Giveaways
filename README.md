# Game giveaways

- Status: In development
- Platforms: Steam
- Features: 
  - Steam:
    - -100% discounted games
    - -100% discounted bundles 
    - -100% discounted DLC-s
    - Temporarily free to access games (aka Free Weekend)

# Information
- Steam: Information gathered from SteamAPI, Steam Store

# Integration

The output follows REST principles, so it needs only iterating over the result:
    Example from `demo.py`

```python
import streamlit as st
from app import App

deals = App.get_deals(steam_free_weekend=True, steam_giveaways=True)
print(deals)

for tag, val in deals.items():
    if not val:
        continue
    else:
        match tag:
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

---
Simplicity and reliability.

---

Armen-Jean Andreasian, 2024