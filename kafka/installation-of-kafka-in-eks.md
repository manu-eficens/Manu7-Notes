
https://github.com/quickbooks2018/kafka-bitnami

eksctl create iamserviceaccount \
  --name ebs-csi-controller-sa \
  --namespace kube-system \
  --cluster canary-eks \
  --attach-policy-arn arn:aws:iam::aws:policy/service-role/AmazonEBSCSIDriverPolicy \
  --approve \
  --role-only \
  --role-name AmazonEKS_EBS_CSI_DriverRole

eksctl create addon --name aws-ebs-csi-driver --cluster canary-eks --service-account-role-arn arn:aws:iam::238393102293:role/AmazonEKS_EBS_CSI_DriverRole --force
