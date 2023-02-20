from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# # .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
# helper_admins = []
IP = env.str("ip")  # Xosting ip manzili
#CHANNELS = ['https://t.me/omonovsanjardev']

BOT_LINKS = "@sehrgar_bot"

DB_CONNECTION_URL = 'postgresql://postgres:i0ZDXc6HhB094j9tgirT@containers-us-west-188.railway.app:6956/railway'

# DB_USER = "postgres"
# DB_PASS = "okPNSpPdglRDqK5LjnrQ"
# DB_NAME = "railway"
# DB_HOST = "containers-us-west-151.railway.app "
# DB_PORT = "6013"
