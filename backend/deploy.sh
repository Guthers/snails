REPO_URL=https://github.com/Guthers/snails.git

SCRATCH_DIR=$(mktemp -d -t scratch-XXXXXXX)

SOURCE_DIR=$SCRATCH_DIR/backend
TARGET_DIR=/var/www/uwsgi

export FLASK_ENV=production

set -e

echo "WARNING: This command will REMOVE and REPLACE /var/www/usgi"
read -r -p "Are you sure? [y/N] " response
case $response in
    [yY]) 
      ;;
    *)
      echo "Aborted"
      exit 1
    ;;
esac

# Clone the repo
git clone $REPO_URL $SCRATCH_DIR

# Stop uwsgi
sudo systemctl stop uwsgi

# Remove old files
rm -rf $TARGET_DIR

# Move files
cp -r $SOURCE_DIR $TARGET_DIR

cd $TARGET_DIR

# Make virtualenv
PIPENV_VENV_IN_PROJECT=True pipenv install

# Populate the db
pipenv run python -m flask populate

# Start uwsgi
sudo systemctl start uwsgi

rm -rf $SCRATCH_DIR

echo ""
echo "Backend dir at /var/www/uwsgi"
echo "UWSGI settings at /etc/uwsgi/uwsgi.ini"
echo "Error log at /var/log/uwsgi/error.log"

