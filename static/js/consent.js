var acceptAllConsent = document.getElementById("accept-all-consent");
var closeConsent = document.getElementById("close-consent");
var containerConsent = document.getElementById("consent-container");
var userAuthenticate = JSON.parse(
  document.getElementById("user-authenticate").textContent
);
var userConsentStatus = JSON.parse(
  document.getElementById("user-consent-status").textContent
);

const updateConsent = async (consentStatus) => {
  return fetch("http://127.0.0.1:8000/update_consent", {
    method: "POST",
    body: consentStatus,
    headers: { "Content-Type": "application/json" },
  });
};

if (userAuthenticate && userConsentStatus !== "GRANTED") {
  containerConsent.style.display = "block";
}

acceptAllConsent.onclick = function () {
  const consentData = {
    consent: {
      typeIdentifier: "first_party",
      scope: "ryr",
      status: "GRANTED",
      statusDate: new Date().toISOString(),
    },
  };
  updateConsent(consentData.consent.status);
  unomiTracker.track("modifyConsent", consentData);
  containerConsent.style.display = "none";
};

closeConsent.onclick = function () {
  const consentData = {
    consent: {
      typeIdentifier: "first_party",
      scope: "ryr",
      status: "DENY",
      statusDate: new Date().toISOString(),
    },
  };
  updateConsent(consentData.consent.status);
  unomiTracker.track("modifyConsent", consentData);
  containerConsent.style.display = "none";
};
