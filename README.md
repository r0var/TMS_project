Here are the files of the TMS course project.  
The app and infra folders were private repositories.  
The files in the jenkins folder were used to install the CI on a separate instance.  
The project was deployed to Linode.
  
In infra, using terraform, I launched four instances and installed a kubernetes cluster on them using kubespray. This pipeline is described in the jenkinsfile.
  
The app contains the python code of the application and the helm chart for deployment. The pipeline describes tests, build and deployment of the application.
