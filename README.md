# It's Game Giveaways!
![cover.png](github%2Fimages%2Fcover.png)
Introducing Game Giveaways, the ultimate toolkit for every gamer!

---
_Game Giveaways is engineered with cutting-edge technologies and industry-leading practices, ensuring a robust and seamless experience for all users. Whether you're a casual gamer or a seasoned developer, Game Giveaways has you covered with three comprehensive solutions tailored to your needs._


---

![info_3.jpg](github%2Fimages%2Finfo_3.jpg)

---
# Overview

- **Giveaways platforms currently supported:** **_Steam_**, **_Epic Games_**
  - Steam:
    - -100% discounted games
    - -100% discounted bundles
    - -100% discounted DLC-s
    - Temporarily free to access games (known as Free Weekend)
  - Epic Games:
    - -100% discounted games
    - -100% discounted DLC-s
    
- **Giveaways platforms will be added soon:** GOG, Alienware Arena, MMO Bomb, Humble Bundle, Fanatical.

---
# Legal advertisement

This project is for demonstration purposes only. 
We do not promote or suggest the use of the techniques shown in the project for any unauthorized or unethical activities. 
We are not responsible for any misuse or illegal actions taken based on the information provided in this project. 
Users are solely responsible for their actions and should adhere to all applicable laws and regulations.

---
# Information Gathering and security

- **Steam**: SteamAPI, Steam Store
  - Protection level: not protected.
- **Epic Games**: Epic Games Store
  - Protection level: anti-bot protection by CloudFlare
 
---

# Program consists of:

1. **Scrapers**:
    - Due to the highest level of abstraction achieved, almost all types of case-specific scrapers are divided by needs and use cases.
    - Two main types of parsers are highlighted for this project:
        - `requests`-based scrapers
          - Are used to request APIs and web sources without protection. These may be replaced with aiohttp in the future if the number of sources grows.
        - `selenium`-based scrapers.
          - Are used to request web sources with possible anti-bot and anti-scraping protections. This is a straightforward, time-tested tool that never disappoints.

2. **Content**:
    - Due to the highest level of abstraction, almost all web content on the internet is managed to be implemented according to its:
        - origin and method of obtaining,
        - type for further analysis and processing.

3. **Cache**:
    - Custom cache designed to be a local key-value in-memory cache, similar to Redis, with timestamp functionality similar to ORM implementations.
    - Naturally, it includes all necessary methods such as 'get', 'reset', and 'update'.
    - For this project, it is programmed to automatically reset after midnight in the USA Eastern Time Zone.

4. **ExceptionLogger**:
    - Custom logger designed to log exceptions with maximum information.

For more detailed information read [documentation.md](docs/documentation.md)

---
# Credits:

Armen-Jean Andreasian, 2024