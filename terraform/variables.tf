variable "project" {
  description = "The GCP project to use"
  type        = string
}

variable "pubsub_topic_name" {
  description = "The name of the Pub/Sub topic"
  type        = string
  default     = "values"
}

variable "region" {
  description = "The GCP region to use"
  type        = string
  default     = "europe-west1"
}
