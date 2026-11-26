import jenkins.model.Jenkins
import hudson.model.User
import hudson.security.HudsonPrivateSecurityRealm

def user = User.getById("anil", false)

if (user == null) {
    throw new Exception("User anil not found")
}

user.addProperty(
    HudsonPrivateSecurityRealm.Details.fromPlainPassword("anil123")
)

user.save()

println("Password reset completed for anil")