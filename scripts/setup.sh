# Error if the build fails
set -e

# Create a virtual environment and install requirements
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt

# Set environment variables
touch .env
echo "EXPORT OPENSKY_USERNAME=gtbigdataclub" >> .env
echo "EXPORT OPENSKY_PASSWORD=<PASSWORD GOES HERE>" >> .env