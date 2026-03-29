# python

python 정리

# ssh-key

```shell
# generate key
ssh-keygen -t ed25519 -C "your_email@example.com"
cat ~/.ssh/id_ed25519.pub

# add ssh key
https://github.com/settings/keys

# test
❯ ssh -T git@github.com
Hi milman2! You've successfully authenticated, but GitHub does not provide shell access.
```
