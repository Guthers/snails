REPO_URL=https://github.com/Guthers/snails.git

SCRATCH_DIR=$(mktemp -d -t scratch-XXXXXXX)

SOURCE_DIR=$SCRATCH_DIR/frontend-board
TARGET_DIR=/var/www/board

set -e

echo "WARNING: This command will REMOVE and REPLACE /var/www/board"
read -r -p "Are you sure? [y/N] " response
case $response in
    [yY]) 
      ;;
    *)
      echo "Aborted"
      exit 1
    ;;
esac


read -r -p "Enter a branch [default=master]: " branch
case $branch in
    "") 
        branch="master"
      ;;
    *)
    ;;
esac

# Clone the repo
git clone $REPO_URL --branch $branch --single-branch $SCRATCH_DIR

cd $SOURCE_DIR

npm install

npm run build

# Remove old files
rm -rf $TARGET_DIR

cp -r $SOURCE_DIR/build $TARGET_DIR

# Fix swaggerdocs
cp -r /var/www/uwsgi/.venv/lib/python3.8/site-packages/flasgger/ui3/static $TARGET_DIR/flasgger_static

rm -rf $SCRATCH_DIR

echo "Success!"
