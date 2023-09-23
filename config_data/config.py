from dataclasses import dataclass
from environs import Env 


@dataclass
class TgBot:
	token: '6055594961:AAEbkzVKH1Yoepk3FqDiT_0v50gwPOreTgw'


@dataclass
class Config:
	tg_bot: TgBot


def load_config(path: str | None = None) -> Config:
	env = Env()
	env.read_env(path)
	return Config(tg_bot=TgBot(token=env('BOT_TOKEN')))