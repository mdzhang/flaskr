# Flaskr (Flask Tutorial)

## Installation

*NB*: Assumes OS X

#### Install [Homebrew](http://brew.sh/#install)

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

#### Checkout the app

```
git clone git@github.com:mdzhang/flaskr.git
cd flaskr
```

#### Install Homebrew packages

```
brew tap Homebrew/bundle
brew bundle
```

#### Configure shell

Update your preferred shell config file with following code and re-execute it in your current shell:

```
if which direnv > /dev/null; then
  eval "$(direnv hook bash)"
fi

if which pyenv > /dev/null; then
  eval "$(pyenv init -)"
fi
```

e.g. you could add this to `~/.bashrc` and then run `$ source .bashrc`

#### Setup development environment variables

```
cp .envrc.sample .envrc
direnv allow
```

#### Install Python

```
pyenv install $(cat ./.python-version)
```

#### Create and activate a virtualenv

```
pyenv virtualenv flaskr
pyenv activate flaskr
```

#### Install Python packages

```
pip install -r requirements/dev.txt
```

#### Install [Git-hooks](https://github.com/git-hooks/git-hooks)

```
git hooks --install
```
