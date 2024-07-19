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
  project = var.project
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

resource "google_storage_bucket" "static_site_bucket" {
  name          = "${var.project}-static-site"
  location      = var.region
  force_destroy = true

  website {
    main_page_suffix = "index.html"
    not_found_page   = "404.html"
  }
}

resource "google_storage_bucket_object" "index" {
  name   = "index.html"
  bucket = google_storage_bucket.static_site_bucket.name
  source = "site/index.html"
  content_type = "text/html"
}

resource "google_storage_bucket_object" "script" {
  name   = "script.js"
  bucket = google_storage_bucket.static_site_bucket.name
  source = "site/script.js"
  content_type = "application/javascript"
}

resource "google_storage_bucket_object" "404" {
  name   = "404.html"
  bucket = google_storage_bucket.static_site_bucket.name
  source = "site/404.html"
  content_type = "text/html"
}
