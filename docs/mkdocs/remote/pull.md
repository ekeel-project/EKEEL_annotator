# Pulling updates from the github repo
----------

## Connect to the Server
```bash
ssh torre@130.251.47.107
# passw: < ask to project administrator >
```

-----
## Update Ekeel App Files from the Repositories

A script named `pull_updates` has been configured inside `/usr/local/bin/` to pull from both the repos at the same time.
```bash
# From anywhere in the console call
sudo pull_updates
```

Otherise use these commands (replica of the script):
```bash
# Navigate to the annotator directory and pull
cd /var/www/apps/annotator
sudo git pull

# Navigate to the augmentator directory and pull
cd /var/www/apps/augmentator
sudo git pull

# username for github: Mirwe
# password: < ask to project administrator >
```
*Note: If github credentials are not valid or you want to use your own credentials...*

!!!warning
    If you made any change to the environment distribution packages then follow [this guide](../platforms/annotator/deploy.md#update-and-setup-video-annotation-app) to update the Annotator or [this guide](../platforms/augmentator/deploy.md#update-and-setup-video-augmentation-app) to update the Augmentator


### Bug: Provided github credentials are not valid
You can use your own github credentials:
```bash
$ git clone https://github.com/...
Username: your_username
Password: your_token # (how to create a personal github access token)
```
A guide on how to do it is [here](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)

-----
## In case of Reinstall

Go in static folder, then create folder videos and give permissions

```bash
cd /var/www/apps/annotator/code/static
# create the folder if you don't have it already
sudo mkdir videos
sudo chmod 777 ./videos
```
