data "google_project" "project" {
  project_id = var.project
}

resource "google_sql_database_instance" "db_instance" {
  name             = "${var.project}-db-instance"
  database_version = "POSTGRES_13"
  region           = var.region

  settings {
    tier = "db-f1-micro"
  }
}

resource "google_sql_database" "db" {
  name     = "level_values_db"
  instance = google_sql_database_instance.db_instance.name
}

resource "google_sql_user" "db_user" {
  name     = "db_user"
  instance = google_sql_database_instance.db_instance.name
  password = "your-password"  # Replace with a secure password
}

provider "google" {
  project = data.google_project.project.project_id
  region  = var.region
}

resource "google_pubsub_topic" "level_values" {
  name = var.pubsub_topic_name
}

resource "google_storage_bucket" "audio_bucket" {
  name     = "${var.project}-audio-bucket"
  location = var.region
  force_destroy = true
}
