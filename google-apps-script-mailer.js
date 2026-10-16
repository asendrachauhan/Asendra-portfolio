/**
 * ============================================================================
 * GOOGLE APPS SCRIPT — MULTI-INBOX ROUTING MAIL FORWARDER
 * ============================================================================
 * 
 * - Recruiter Contact Form Messages -> asendrachauhan176@gmail.com
 * - Real Human Visitor Notifications -> asendrachauhan175@gmail.com
 * - 100% of crawlers, bots & cloud datacenters silently filtered
 * ============================================================================
 */

const CONTACT_EMAIL = "asendrachauhan176@gmail.com";
const VISITOR_EMAIL = "asendrachauhan175@gmail.com";

function doPost(e) {
  try {
    const contents = e.postData ? JSON.parse(e.postData.contents) : {};

    const isVisit = !!(
      contents.location || 
      contents.browser || 
      contents.operating_system ||
      contents.os || 
      contents.page_visited ||
      contents.internet_provider ||
      (contents._subject && contents._subject.includes('VISIT'))
    );

    // ==========================================
    // 1. VISITOR NOTIFICATIONS -> asendrachauhan175@gmail.com
    // ==========================================
    if (isVisit) {
      // Reject datacenter, hosting, or bot reports on server side
      const net = ((contents.internet_provider || contents.network_provider || "") + " " + (contents.location || "") + " " + (contents.operating_system || contents.os || "") + " " + (contents.browser || "")).toLowerCase();
      const isDatacenterOrBot = /microsoft|azure|amazon|aws|google|datacenter|hosting|digitalocean|cloudflare|ovh|hetzner|linode|vultr|datacamp|chase city|quadranet|choopa|m247|cogent|server|vps|bot|crawl|spider|headless|puppeteer|selenium|playwright/i.test(net);
      
      if (isDatacenterOrBot) {
        return ContentService.createTextOutput(JSON.stringify({
          success: true,
          filtered: true,
          message: "Filtered: Crawler or cloud datacenter visit ignored"
        })).setMimeType(ContentService.MimeType.JSON);
      }

      // Send visitor alert ONLY to asendrachauhan175@gmail.com
      const recipient = VISITOR_EMAIL;
      const rawSubject = contents._subject || ("[PORTFOLIO VISIT] " + (contents.location || "Verified Visitor"));
      const subject = rawSubject.replace(/\uFFFD/g, "").trim() || "[PORTFOLIO VISIT]";

      let htmlBody = "<div style='font-family:system-ui,-apple-system,sans-serif;padding:24px;max-width:600px;border:1px solid #e2e8f0;border-radius:12px;background:#ffffff;'>";
      htmlBody += "<div style='display:inline-block;padding:4px 10px;background:#0f172a;color:#10b981;font-weight:700;font-size:11px;letter-spacing:1px;border-radius:6px;text-transform:uppercase;margin-bottom:12px;'>VERIFIED REAL VISITOR</div>";
      htmlBody += "<h2 style='color:#0f172a;margin-top:0;margin-bottom:16px;font-size:18px;'>" + subject + "</h2>";
      htmlBody += "<table style='width:100%;border-collapse:collapse;margin-top:15px;'>";
      
      for (const key in contents) {
        if (key.startsWith("_")) continue;
        htmlBody += "<tr>";
        htmlBody += "<td style='padding:8px 12px;border-bottom:1px solid #f1f5f9;color:#64748b;font-weight:600;font-size:12px;text-transform:uppercase;'>" + key.replace(/_/g, ' ') + "</td>";
        htmlBody += "<td style='padding:8px 12px;border-bottom:1px solid #f1f5f9;color:#1e293b;font-size:14px;'>" + contents[key] + "</td>";
        htmlBody += "</tr>";
      }
      htmlBody += "</table>";
      htmlBody += "<p style='font-size:11px;color:#94a3b8;margin-top:20px;'>Sent automatically to asendrachauhan175@gmail.com from your Asendra Portfolio.</p>";
      htmlBody += "</div>";

      GmailApp.sendEmail(recipient, subject, "New verified visitor from " + (contents.location || "unknown"), {
        htmlBody: htmlBody
      });

      return ContentService.createTextOutput(JSON.stringify({
        success: true,
        message: "Visitor alert sent to " + VISITOR_EMAIL
      })).setMimeType(ContentService.MimeType.JSON);
    }

    // ==========================================
    // 2. CONTACT FORM MESSAGES -> asendrachauhan176@gmail.com
    // ==========================================
    const name = contents.name || "Anonymous Visitor";
    const email = contents.email || "No email provided";
    const message = contents.message || "";

    // Clean subject line for contact message
    let rawSubject = contents._subject || ("[PORTFOLIO CONTACT] " + name + (email && email.includes("@") ? " (" + email + ")" : ""));
    const subject = rawSubject.replace(/\uFFFD/g, "").trim() || ("[PORTFOLIO CONTACT] " + name);

    let htmlBody = "<div style='font-family:system-ui,-apple-system,sans-serif;padding:24px;max-width:600px;border:1px solid #e2e8f0;border-radius:12px;background:#ffffff;'>";
    htmlBody += "<div style='display:inline-block;padding:4px 10px;background:#0f172a;color:#10b981;font-weight:700;font-size:11px;letter-spacing:1px;border-radius:6px;text-transform:uppercase;margin-bottom:12px;'>NEW PORTFOLIO MESSAGE</div>";
    htmlBody += "<h2 style='color:#0f172a;margin-top:0;margin-bottom:16px;font-size:18px;'>" + subject + "</h2>";
    htmlBody += "<table style='width:100%;border-collapse:collapse;margin-top:15px;'>";

    for (const key in contents) {
      if (key.startsWith("_")) continue;
      const val = contents[key];
      htmlBody += "<tr>";
      htmlBody += "<td style='padding:8px 12px;border-bottom:1px solid #f1f5f9;color:#64748b;font-weight:600;font-size:12px;text-transform:uppercase;'>" + key.replace(/_/g, ' ') + "</td>";
      htmlBody += "<td style='padding:8px 12px;border-bottom:1px solid #f1f5f9;color:#1e293b;font-size:14px;'>" + val + "</td>";
      htmlBody += "</tr>";
    }

    htmlBody += "</table>";
    htmlBody += "<p style='font-size:11px;color:#94a3b8;margin-top:20px;'>Sent automatically to asendrachauhan176@gmail.com from your Asendra Portfolio.</p>";
    htmlBody += "</div>";

    // Send email via Gmail to CONTACT_EMAIL
    GmailApp.sendEmail(CONTACT_EMAIL, subject, message || "New transmission received.", {
      htmlBody: htmlBody,
      replyTo: (email && email.includes("@")) ? email : undefined
    });

    return ContentService.createTextOutput(JSON.stringify({
      success: true,
      message: "Contact message dispatched to " + CONTACT_EMAIL
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
