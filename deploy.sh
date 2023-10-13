git com &&
git reset --hard 40213a9a9e5c3578188b5e4880d2c7b0e34ef3ab &&
git merge --squash draft-presentation &&
git rm -rf _archive _notebook_as_py deploy.sh
git commit -m "Add files" &&
git push -f
