# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

  config.vm.box = "iamseth/rhel-6.8-x86_64"

  config.vm.network "forwarded_port", guest: 5009, host: 5009, host_ip: "127.0.0.1"
  config.vm.network "forwarded_port", guest: 80, host: 8009, host_ip: "127.0.0.1"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
    vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
  end

  config.vm.network "private_network", ip: "192.168.22.66"
  config.vm.synced_folder "./", "/vagrant", owner: 'vagrant', group: 'vagrant', mount_options: ["dmode=775,fmode=775"]
  config.vm.provision "shell", path: "scripts/provision_vagrant.sh"
end
