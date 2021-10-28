FROM jenkins/jenkins:2.290

ARG HELM_VERSION=3.5.4
ARG DEBIAN_FRONTEND=noninteractive
ARG ANSIBLE_VERSION=2.10.7

RUN /usr/local/bin/install-plugins.sh ssh-slaves \
  ansible \
  artifact-manager-s3 \
  email-ext \
  mailer \
  greenballs \
  simple-theme-plugin \
  parameterized-trigger \
  rebuild \
  github \
  mask-passwords \
  kubernetes \
  docker-plugin \
  slack \
  docker-workflow \
  blueocean \
  stashNotifier \
  show-build-parameters \
  credentials \
  configuration-as-code \
  command-launcher \
  external-monitor-job \
  ssh-agent \
  pipeline-stage-view

USER root
RUN apt-get update && apt-get install -y apt-transport-https \
  # python-pip \
  python3-pip \
  ca-certificates \
  curl \
  gnupg2 \
  software-properties-common \
  && wget https://get.helm.sh/helm-v${HELM_VERSION}-linux-amd64.tar.gz -P /tmp/ > /dev/null \
  && tar -zxvf /tmp/helm-v${HELM_VERSION}-linux-amd64.tar.gz --directory /tmp/ \
  && mv /tmp/linux-amd64/helm /usr/local/bin/helm \
  && curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - \
  && touch /etc/apt/sources.list.d/kubernetes.list \
  && echo "deb http://apt.kubernetes.io/ kubernetes-xenial main" | tee -a /etc/apt/sources.list.d/kubernetes.list \
  && curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg > /tmp/dkey; apt-key add /tmp/dkey \
  && add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") \
    $(lsb_release -cs) \
    stable" \
  && curl -fsSL https://apt.releases.hashicorp.com/gpg | apt-key add - \
  && apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main" \
  && apt-get update \
  && apt-get install -y terraform \
  && apt-get install -y kubectl \
  && pip3 install boto3 \
    botocore \
      # ansible==${ANSIBLE_VERSION} \
    # molecule \
    awscli \
    cryptography \
    netaddr \
    pylint \
  && pip3 install "ansible-lint[yamllint]" \
      ansible==${ANSIBLE_VERSION} \
  && git config --global core.sshCommand 'ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no' \
  && apt-get -y install docker-ce-cli \
  && apt-get install rsync -y \
  && echo "    StrictHostKeyChecking no" >> /etc/ssh/ssh_config \
  && echo "    UserKnownHostsFile=/dev/null" >> /etc/ssh/ssh_config \
  && apt-get purge --auto-remove -yqq \
  && apt-get clean \
  && rm -rf \
    /var/lib/apt/lists/* \
    /tmp/* \
    /var/tmp/* \
    /usr/share/man \
    /usr/share/doc \
    /usr/share/doc-base

USER jenkins
