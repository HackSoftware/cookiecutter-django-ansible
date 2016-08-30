# Ansible documentation.

## What is this repository?

Our machines are provisioned and maintained **ONLY with ansible roles**. So if you want to make any changes to the machines **DONT DO IT VIA SSH**. Make changes in this repo and run the ansible code to change the server state. 

**What this ansible code do?**

- It installs python.
- It sends the team keys to the server.
- It installs the postgresql server and configures it.
- It installs the nginx server and configures the vhost.
- It configures everyting that django needs: directory structure, upstart jobs, env vars, etc.

## Why do we use ansible?
Using ansible, we have dramatically reduced the time it takes us to deliver applications into production, from weeks to days and even hours.

Eliminate Configuration Drift - With ansible, our servers remain in the state we set for them.

Visibility - Ansible gives us rich data sets not only of infrastructure configuration but also of any changes to that infrastructure. We have much more visibility into the changes occurring in our infrastructure over time and their impact to service levels

Ansible can provision a fully working server in 20 minutes. That would have taken close to a full day of work without ansible!

## How to run the ansible code?
First of all you need to have latest ansible installed.


```
$ pip install ansible
```

Then you have to install all ansible roles. ``ansible-galaxy`` is the package manager here.

```
$ ansible-galaxy install -r requirements.yml
```

### And now you are ready to run the ansible code

You can run the ansible code in a vagrant virtual box just to test it. **Always test your code in a virtual box before running it in production!**

```
vagrant up
```

**Lets run the vagrant code in production**

Provision the staging server

```
ansible-playbook -i staging sites.yml
```

Provision the production server

```
ansible-playbook -i production site.yml
```

## Common things that you can change here.

### Change the machine IP address or add a new machine

We have two types of machines: webservers and dbservers. That makes scaling easyer but you can use the same machine for both types.

Here are the machines addresses:
- [Staging machines](/staging)
- [Production machines](/production)

### Nginx configuration

Maybe you want to change the nginx config? [It is here.](/roles/application/templates/nginx_config.j2)

### SSH Keys

Maybe you want to give someone access to the server? [Look at this dir.](/ansible_vars/public_keys/)

### Django related changes

#### Change some env vars

There are two env configuration. One for your production server and one for your staging server. [The env files are located here.](/application_vars/)

#### See sensible information
All sensible informatin like passwords for postgres and rabbitmq can be changed from [here.](/ansible_vars/)