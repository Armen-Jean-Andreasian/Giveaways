import streamlit as st
from src.app import App


def set_up_frontend():
    st.set_page_config(
        page_icon="https://static.vecteezy.com/system/resources/previews/017/744/677/original/video-game-icon-png.png")

    video_html = """
        <style>
            #myVideo {
                position: fixed;
                right: 0;
                bottom: 0;
                min-width: 100%; 
                min-height: 100%;
            }
        </style>	
        <video autoplay muted loop id="myVideo">
            <source src="https://videos.pexels.com/video-files/4990245/4990245-hd_1920_1080_30fps.mp4" type="video/mp4">
        </video>
    """
    st.markdown(video_html, unsafe_allow_html=True)

    st.subheader('Game giveaways')
    tab1, tab2, tab3 = st.tabs(["Steam Giveaways", "Steam Free Weekend", "Epic Games Giveaways"])
    return tab1, tab2, tab3


def display_giveaway_content(giveaway: dict):
    """ Displays the content of a single giveaway. """
    st.text(f"{giveaway['game_name']}")
    st.image(giveaway['rectangle_img_url'], width=300)
    st.link_button(label="Open Giveaway", url=giveaway['game_url'])
    st.divider()


def display_giveaways(deals: dict, tab1, tab2, tab3):
    """ Display giveaways in respective tabs."""
    for key, giveaways in deals.items():
        for giveaway in giveaways:
            if key == 'steam_giveaways':
                with tab1:
                    display_giveaway_content(giveaway)
            elif key == 'steam_free_weekend':
                with tab2:
                    display_giveaway_content(giveaway)
            elif key == 'epic_games_giveaways':
                with tab3:
                    display_giveaway_content(giveaway)


def main():
    # Fetch deals
    deals = App.get_deals(steam_free_weekend=True, steam_giveaways=True, epic_games_giveaways=True)

    # Set up frontend
    tab1, tab2, tab3 = set_up_frontend()

    # Display giveaways
    display_giveaways(deals, tab1, tab2, tab3)


if __name__ == '__main__':
    main()
