# STEPS:

## STEP 01: Create a empty remote repository

## STEP 02: Intialize a git local repository and connect to repository

* open and project folder  in vs code the follow below command -

```bash
git init
git add . 
git commit -m "comment"
git branch -M main
git remote add origin git_url
git push -u origin main
```

## STEP 03: create and activate conda enviremnt

```bash
conda create -n env_name python=3.7 -y
conda activate env_name

```

### creating files using touch ,"touch will work only git bash or mac and linux"
```touch file_name```

## step 04 initialize dvc
```
dvc init
```

## Create  the basice directory structure
```bash
mkdir -p src/utils
```
