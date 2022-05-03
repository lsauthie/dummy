class User:
    def __init__(self, id_token_claims):
        self.id = id_token_claims.get("oid")
        self.display_name = id_token_claims.get("name")
        self.first_name = id_token_claims.get("given_name")
        self.surname = id_token_claims.get("family_name")
        self.emails = id_token_claims.get("emails")
        self.job_title = id_token_claims.get("jobTitle")