from locust import HttpUser, task, between

class WebsitePerformanceTest(HttpUser):
    wait_time = between(1, 3)  # Simule un délai d'attente entre les actions des utilisateurs

    @task
    def homepage_test(self):
        """Test de la page d'accueil."""
        self.client.get("/")  # Route pour la page d'accueil

    @task
    def about_page_test(self):
        """Test de la page 'À propos'."""
        self.client.get("/about/")  # Route pour la page 'À propos'

    @task
    def subscribe_newsletter_test(self):
        """Simule l'abonnement à la newsletter."""
        self.client.post("/subscribe_newsletter/", data={
            'email': 'testuser@example.com'
        })  # Remplacez cette route et les données par celles de votre application

    @task
    def social_count_test(self):
        """Test des interactions sociales (like/share)."""
        self.client.post("/social_count/", data={
            'action': 'like',  # Exemple d'action
            'post_id': 1       # Remplacez par un ID valide
        })

    @task
    def site_info_test(self):
        """Test pour obtenir les informations du site."""
        self.client.get("/site_info/")  # Remplacez par une route qui existe dans votre projet

    @task
    def invalid_page_test(self):
        """Test pour une page inexistante (vérifier les erreurs 404)."""
        self.client.get("/invalid_page/")  # Test pour une route inexistante

    @task
    def user_registration_test(self):
        """Simule l'enregistrement d'un utilisateur."""
        self.client.post("/register/", data={
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'password1234',
            'password2': 'password1234'
        })  # Remplacez avec les champs spécifiques à votre formulaire

    @task
    def user_login_test(self):
        """Simule la connexion d'un utilisateur."""
        self.client.post("/login/", data={
            'username': 'testuser',
            'password': 'password1234'
        })  # Remplacez avec les champs spécifiques à votre formulaire

    @task
    def newsletter_unsubscribe_test(self):
        """Simule la désinscription à la newsletter."""
        self.client.post("/unsubscribe_newsletter/", data={
            'email': 'testuser@example.com'
        })  # Remplacez par votre route de désinscription
