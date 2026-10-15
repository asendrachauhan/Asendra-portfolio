/**
 * ============================================================================
 * GOOGLE APPS SCRIPT — 100% FREE, PRIVATE EMAIL FORWARDER FOR YOUR PORTFOLIO
 * ============================================================================
 * 
 * Want completely private, unlimited emails sent straight from your own Gmail?
 * Google Apps Script lets you run a free webhook that forwards messages using
 * your personal Gmail quota (up to 500 emails/day free forever!).
 *
 * HOW TO SET THIS UP IN 2 MINUTES:
 * ----------------------------------------------------------------------------
 * 1. Open https://script.google.com and click "New project".
 * 2. Delete any existing code, paste the contents of this file, and click Save (💾).
 * 3. Click the blue "Deploy" button at the top right -> "New deployment".
 * 4. Select type: "Web app" (click the gear icon ⚙️ if not selected).
 * 5. Configure:
 *    - Description: "Portfolio Contact Mailer"
 *    - Execute as: "Me (your email)"
 *    - Who has access: "Anyone" (crucial so your portfolio can post to it)
 * 6. Click "Deploy" and authorize access with your Google account.
 * 7. Copy the "Web app URL" (looks like: https://script.google.com/macros/s/.../exec).
 * 8. Open index.html in your portfolio and set:
 *    window.ASENDRA_CUSTOM_ENDPOINT = "https://script.google.com/macros/s/YOUR_DEPLOYMENT_ID/exec";
 *
 * That's it! Your contact form and visitor telemetry will now post directly
 * to your Google Apps Script, sending clean emails straight to your inbox.
 * ============================================================================
 */

const RECIPIENT_EMAIL = "asendrachauhan176@gmail.com";

function doPost(e) {
  try {
    const contents = e.postData ? JSON.parse(e.postData.contents) : {};
    
    const isVisit = !!contents.location;

    // Filter out bots, crawlers, and cloud datacenters (Chase City, Azure, AWS, GCP, etc.)
    if (isVisit) {
      const net = ((contents.network_provider || "") + " " + (contents.location || "") + " " + (contents.os || "") + " " + (contents.browser || "")).toLowerCase();
      const isDatacenterOrBot = /microsoft|azure|amazon|aws|google|datacenter|hosting|digitalocean|cloudflare|ovh|hetzner|linode|vultr|datacamp|chase city|bot|crawl|spider|headless|puppeteer|selenium|playwright/i.test(net);
      if (isDatacenterOrBot) {
        return ContentService.createTextOutput(JSON.stringify({
          success: true,
          filtered: true,
          message: "Filtered: Automated crawler or datacenter visit suppressed"
        })).setMimeType(ContentService.MimeType.JSON);
      }
    }

    const name = contents.name || "Anonymous Visitor";
    const email = contents.email || "No email provided";
    const message = contents.message || "";

    // Clean subject line: strip any Unicode replacement characters (\uFFFD) or surrogate pairs
    let rawSubject = contents._subject || (isVisit 
      ? ("[PORTFOLIO VISIT] " + (contents.location || "Unknown")) 
      : ("[PORTFOLIO CONTACT] " + name + (email && email.includes("@") ? " (" + email + ")" : "")));
    
    const subject = rawSubject.replace(/[\uFFFD\uD800-\uDBFF\uDC00-\uDFFF]/g, '').trim() || 
      (isVisit ? "[PORTFOLIO VISIT]" : "[PORTFOLIO CONTACT] " + name);

    let htmlBody = "<div style='font-family:system-ui,-apple-system,sans-serif;padding:24px;max-width:600px;border:1px solid #e2e8f0;border-radius:12px;background:#ffffff;'>";
    htmlBody += "<div style='display:inline-block;padding:4px 10px;background:#0f172a;color:#10b981;font-weight:700;font-size:11px;letter-spacing:1px;border-radius:6px;text-transform:uppercase;margin-bottom:12px;'>" + (isVisit ? "VISITOR TELEMETRY" : "NEW PORTFOLIO MESSAGE") + "</div>";
    htmlBody += "<h2 style='color:#0f172a;margin-top:0;margin-bottom:16px;font-size:18px;'>" + subject + "</h2>";
    htmlBody += "<table style='width:100%;border-collapse:collapse;margin-top:15px;'>";

    for (const key in contents) {
      if (key.startsWith("_")) continue;
      const val = contents[key];
      htmlBody += "<tr>";
      htmlBody += "<td style='padding:8px 12px;border-bottom:1px solid #f1f5f9;color:#64748b;font-weight:600;font-size:12px;text-transform:uppercase;'>" + key + "</td>";
      htmlBody += "<td style='padding:8px 12px;border-bottom:1px solid #f1f5f9;color:#1e293b;font-size:14px;'>" + val + "</td>";
      htmlBody += "</tr>";
    }

    htmlBody += "</table>";
    htmlBody += "<p style='font-size:11px;color:#94a3b8;margin-top:20px;'>Sent automatically from your Asendra Portfolio.</p>";
    htmlBody += "</div>";

    // Send email via Gmail
    GmailApp.sendEmail(RECIPIENT_EMAIL, subject, message || "New transmission received.", {
      htmlBody: htmlBody,
      replyTo: (email && email.includes("@")) ? email : undefined
    });

    return ContentService.createTextOutput(JSON.stringify({
      success: true,
      message: "Email dispatched successfully"
    })).setMimeType(ContentService.MimeType.JSON);

  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({
      success: false,
      error: err.toString()
    })).setMimeType(ContentService.MimeType.JSON);
  }
}

function doGet(e) {
  return ContentService.createTextOutput("Asendra Portfolio Mailer is active and operational.")
    .setMimeType(ContentService.MimeType.TEXT);
}
