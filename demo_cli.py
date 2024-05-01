from src.app import App
# from utils.debugging import save_json

deals = App.get_deals(steam_free_weekend=True, steam_giveaways=True, epic_games_giveaways=True)
# save_json(content=deals, file_name='test')

print(deals)
