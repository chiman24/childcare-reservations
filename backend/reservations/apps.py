from django.apps import AppConfig

print("DEBUG DEBUG DEBUG in reservations.apps.py")


class ReservationsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "reservations"

    def ready(self):
        print("📦 ReservationsConfig.ready() called")
        try:
            import reservations.mongo_config
            print("🔌 MongoDB connection established.")
        except Exception as e:
            print(f"Error importing mongo_config: {e}")
