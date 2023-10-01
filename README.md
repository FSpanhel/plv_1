- [Data Science Challenge](#data-science-challenge)
- [Repo Structure](#repo-structure)
- [Package Documentation](#package-documentation)
- [Installation](#installation)
  - [Cloning the Git repo](#cloning-the-git-repo)
  - [Creating and activating the environment](#creating-and-activating-the-environment)
  - [Configuring and starting notebook servers](#configuring-and-starting-notebook-servers)
  - [Getting data that is not versioned by Git](#getting-data-that-is-not-versioned-by-git)
- [Note](#note)

# Data Science Challenge

- This repo provides all materials for this course.
- Information about the course can be found in [COURSE.md](COURSE.md).
- Note that notebooks or other code in this repo should be run in the corresponding [environment](#creating-and-activating-the-environment).

# Repo Structure
Description of relevant folders and files:
```
├── AUTHORS.md              <- List of developers and maintainers.
├── CHANGELOG.md            <- Changelog to keep track of updates.
├── CONTRIBUTING.md         <- Guidelines for contributing to this project.
├── COURSE.md               <- Information about the course.
├── LICENSE.txt             <- License.
├── README.md               <- The top-level README.
├── data                    <- Data should be placed here.
├── docs                    <- Documentation of the `dsc` package.
├── environment.yml         <- The conda environment file.
├── lecture_notes           <- Contains the lecture notes that will be presented.
├── src/dsc                 <- Python package that is used for this course.
```

# Package Documentation
Open the [docs](docs/index.html) with a browser to see the documentation of the package of this repo.

# Installation
## Cloning the Git repo
To copy this remote repository to a local repository you need [Git] which should already be installed if you are using a unix-based OS.

If your OS is Windows you can use [WSL] or [Git For Windows].
- I highly recommend to use [WSL].
- You can easily access [WSL] via [VSCode] using the [remote extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack).
- Click [here](https://code.visualstudio.com/docs/remote/remote-overview) for more information.


To clone the repo with SSH into the current working directory
- [Set up SSH keys to communicate with GitLab](https://docs.gitlab.com/ee/user/ssh.html).
- Run the following command in the terminal.
    ```sh
    git clone git@gitlab.lrz.de:dsc/2023/course.git
    ```

Alternatively, you can clone with HTTPS using
```sh
git clone https://gitlab.lrz.de/dsc/2023/course.git
```


## Creating and activating the environment
- In order to set up the necessary environment you need [(mini)conda](https://docs.conda.io/en/latest/miniconda.html) (or [mamba]).
- From the root directory of the cloned Git repo, you can create the 'dsc' environment by running  ```conda env create -f environment.yml``` in the terminal.
- You can activate the environment using ```conda activate dsc```.  
- You should **always activate the environment** when you want to run code of this Git repo or want to use the `dsc` package.
- If you are using VS Code you can find [here](https://code.visualstudio.com/docs/python/environments#_work-with-python-interpreters) instructions how to automatically activate the environment when you open the dsc folder with VS Code.

Note: If something like ```python3 -m dsc...``` does not run, please run ```pip install -e .``` from the root of this repo.

## Configuring and starting notebook servers
- First of all, activate the `dsc` environment in the terminal.
- To set the notebook extensions, run ```python3 -m dsc.notebook``` in the terminal.
- Run ```jupyter notebook``` in the terminal to start a notebook server that can be accessed via a browser.
- To present notebooks located in the folder `lecture_notes` as slides press `alt + r`.
- Press `alt + r` again to exit slide mode.
- You might need to zoom out so that everything is visible on a slide.

<!-- pyscaffold-notes -->

## Getting data that is not versioned by Git
- Email your Gmail address to spanhelhm@gmail.com
    - In case you don't have a Google account, please [create an account](https://accounts.google.com/).
    - If you don't want to provide your email or phone number you can use throw-away accounts.
- Login to [Gdrive](https://drive.google.com/drive) and check if Fabian Spanhel has shared the folder `origin` with you.
- From an activated `dsc` environment run `dvc pull` in the terminal.
- You will now be prompted to visit a Google authentication web page.
    - See the section 11.3.1 of [lectures_notes/0_introduction/0_intro.ipynb]([lectures_notes/0_introduction/0_intro.ipynb) how to access this web page if you are using WSL.
- Sign in with the Gmail address that you have sent to spanhelhm@gmail.com and check `Select all` on the following webpage.
- If the authentication was successful, the file `data/dsc.db` should now exist.

# Note

This project has been set up using [PyScaffold] 4.3.1.

[conda]: https://docs.conda.io/
[mamba]: https://github.com/mamba-org/mamba
[PyScaffold]: https://pyscaffold.org/
[Git]: https://git-scm.com/
[Git for Windows]: https://gitforwindows.org/
[WSL]: https://learn.microsoft.com/en-us/windows/wsl/install
[VSCode]: https://code.visualstudio.com/
