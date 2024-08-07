import toml

class PlatformConfig:
    def __init__(self, youtube, twitch):
        self.youtube = youtube
        self.twitch = twitch

class YoutubeConfig:
    def __init__(self, api_key, enabled_features):
        self.api_key = api_key
        self.enabled_features = enabled_features

class TwitchConfig:
    def __init__(self, client_id, client_secret, redirect_uri, oauth2_port):
        self.client_id = client_id
        self.client_secret = client_secret
        self.oauth2_port = oauth2_port
        self.redirect_uri = redirect_uri

class DatabaseConfig:
    def __init__(self, connection_string):
        self.connection_string = connection_string

class BotConfig:
    def __init__(self, client_id, prefix, bot_token, state, status, status_delay, delete_response_emoji):
        self.client_id = client_id
        self.prefix = prefix
        self.bot_token = bot_token
        self.state = state
        self.status = status
        self.status_delay = status_delay
        self.delete_response_emoji = delete_response_emoji

class Status:
    def __init__(self, type, name):
        self.type = type
        self.name = name

class LoggingConfig:
    def __init__(self, level, out_dir, webhook=None):
        self.level = level
        self.out_dir = out_dir
        self.webhook = webhook

class WebhookConfig:
    def __init__(self, enabled, level, url):
        self.enabled = enabled
        self.level = level
        self.url = url

class ServicesConfig:
    def __init__(self, youtube, twitch):
        self.youtube = youtube
        self.twitch = twitch

class YoutubeServicesConfig:
    def __init__(self, dynamic_channel_message_info, dynamic_channel_vcname_info, channel_releases, milestone_notifications):
        self.dynamic_channel_message_info = dynamic_channel_message_info
        self.dynamic_channel_vcname_info = dynamic_channel_vcname_info
        self.channel_releases = channel_releases
        self.milestone_notifications = milestone_notifications

class TwitchServicesConfig:
    def __init__(self, dynamic_channel_message_info, dynamic_channel_vcname_info, milestone_notifications, event_notifications):
        self.dynamic_channel_message_info = dynamic_channel_message_info
        self.dynamic_channel_vcname_info = dynamic_channel_vcname_info
        self.milestone_notifications = milestone_notifications
        self.event_notifications = event_notifications

class ColorsConfig:
    def __init__(self, primary, secondary, success, error, invis):
        self.primary = primary
        self.secondary = secondary
        self.success = success
        self.error = error
        self.invis = invis

def load_config():
    with open('config/config.toml', 'r', encoding="utf-8") as f:
        config_data = toml.load(f)

    platform = PlatformConfig(
        youtube=YoutubeConfig(**config_data['platform']['youtube']),
        twitch=TwitchConfig(**config_data['platform']['twitch'])
    )

    database = DatabaseConfig(connection_string=config_data['database']['connection_string'])

    bot = BotConfig(**config_data['bot'])

    webhook_config_data = config_data['logging'].pop('webhook', None)
    logging = LoggingConfig(**config_data['logging'], webhook=WebhookConfig(**webhook_config_data) if webhook_config_data else None)

    services = ServicesConfig(
        youtube=YoutubeServicesConfig(**config_data['services']['youtube']),
        twitch=TwitchServicesConfig(**config_data['services']['twitch'])
    )

    colors = ColorsConfig(**config_data['colors'])

    return platform, database, bot, logging, services, colors