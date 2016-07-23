# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"
  
  config.vm.provider "virtualbox" do |v|
    v.memory = 2048
    v.cpus = 2
  end
 
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "vagrant.yml"
    ansible.verbose = "vv"
  end
end
