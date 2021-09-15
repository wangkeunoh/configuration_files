# WG's configuration_files

## Install neovim, tmux, fzf, ripgrep
sudo apt update \
sudo apt install neovim (https://github.com/neovim/neovim/wiki/Installing-Neovim) \
sudo apt install tmux \
sudo apt-get install fzf (https://github.com/junegunn/fzf) \
sudo apt-get install ripgrep (https://github.com/BurntSushi/ripgrep) 


## Install Vim-Plug 
curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs \
  https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim


## Fecth config files
cd ~/.config \
git clone https://github.com/wangkeunoh/configuration_files nvim \
cp tmux.conf ~/.tmux.conf \
cp -r tmux ~/.tmux
