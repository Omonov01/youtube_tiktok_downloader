from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# # .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxat
IP = env.str("ip")  # Xosting ip manzili
BOT_LINKS = "@sehrgar_bot"

#DB_CONNECTION_URL = "postgresql://postgres:4wnzB0ekmbUf3xaFIq58@containers-us-west-151.railway.app:6735/railway"
DATABASE_URL = "postgresql://postgres:4wnzB0ekmbUf3xaFIq58@containers-us-west-151.railway.app:6735/railway"
PGDATABASE  = "railway"
PGHOST = "containers-us-west-151.railway.app"
PGPASSWORD = "4wnzB0ekmbUf3xaFIq58"
PGPORT = "6735"
PGUSER = "postgres" 







