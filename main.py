import os
from beem import Hive
from beem.comment import Comment
import json

# --- SECRETS CONFIGURATION ---
# Kinukuha ang sensitive data mula sa Heroku Config Vars
TEST_KEY = os.environ.get('TIP_BOT_KEY') 
TEST_USERNAME = os.environ.get('TIP_BOT_USERNAME')

# --- HIVE AND GEO-FENCING CONFIG ---
HIVE_NODES = ['https://api.hive.blog', 'https://api.openhive.network']
client = Hive(node=HIVE_NODES, keys=[TEST_KEY])

# Target Post Identifier (Gagamitin lang sa testing)
POST_IDENTIFIER = "@marvinvelasquez/palawan-expedition-day-1-el-nido"

# Geo-Fencing Boundary (Palawan Example)
PALAWAN_LAT_MIN = 8.5
PALAWAN_LAT_MAX = 12.0
PALAWAN_LON_MIN = 117.0
PALAWAN_LON_MAX = 120.0

# --- MAIN VERIFICATION FUNCTION ---
def verify_and_mint_pin(post_id):
    if not TEST_KEY or not TEST_USERNAME:
        return "ERROR: TIP_BOT_KEY or TIP_BOT_USERNAME not set in Config Vars."

    try:
        # 1. I-access ang post data
        post = Comment(post_id, hive_instance=client)

        if not post.exists():
            return f"❌ ERROR: Post does not exist or is deleted: {post_id}"

        # 2. I-parse ang JSON metadata
        metadata = json.loads(post['json_metadata'])
        
        # ... (REST OF THE GEO-FENCING LOGIC) ...
        # ... (SIMULATED MINTING PAYLOAD LOGIC) ...
        
        # Example Simulation of SUCCESS:
        mint_payload = {
            'symbol': 'TIP-PLW',
            'to': post['author'],
            'properties': {'name': "Palawan Pin", 'location': 'Palawan'}
        }
        return f"✅ SUCCESS! Minting Payload Generated: {mint_payload}"

            
    except Exception as e:
        return f"❌ FATAL ERROR during verification: {e}"

# --- RUN SCRIPT (Kailangang tumakbo ang function na ito sa Heroku) ---
if __name__ == "__main__":
    result = verify_and_mint_pin(POST_IDENTIFIER)
    print("---------------------------------------")
    print("TIP Verification Bot Log:")
    print(result)
    print("---------------------------------------")
