import streamlit as st
import os
from pathlib import Path

# Configure page
st.set_page_config(
    page_title="🧠 Automation Suite",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for dark theme and styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        color: white;
    }
    
    .category-card {
        background: #1e1e1e;
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid #333;
        margin: 1rem 0;
        transition: transform 0.2s;
    }
    
    .category-card:hover {
        transform: translateY(-2px);
        border-color: #4CAF50;
    }
    
    .task-button {
        background: #2d2d2d;
        border: 1px solid #444;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem;
        text-align: center;
        cursor: pointer;
        transition: all 0.2s;
    }
    
    .task-button:hover {
        background: #3d3d3d;
        border-color: #4CAF50;
    }
    
    .stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #4CAF50 0%, #45a049 100%);
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        font-weight: bold;
    }
    
    .sidebar .sidebar-content {
        background: #1a1a1a;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🧠 Automation Suite</h1>
        <h3>Unified Control Dashboard</h3>
        <p>Welcome to your modular command center. Select a tool from the sidebar to get started.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar navigation with categories
    st.sidebar.title("🧠 Automation Suite")
    
    # Category selection
    category = st.sidebar.selectbox("Select Category:", 
                                   ["🔧 Python Automation", "🟨 JavaScript Tools", "🐧 Linux"])
    
    # Navigation tabs based on category
    if category == "🔧 Python Automation":
        tabs = ["🔔 Notifications", "🌐 Web Scraper", "🔍 Google Search", "📧 Email Sender", 
                "🎨 Image Generator", "🔄 Face Swap", "💬 WhatsApp", "📱 SMS Sender", 
                "📞 Phone Caller", "🖥 RAM Monitor", "📲 WhatsApp Anonymous", "📚 Tuple vs List"]
    elif category == "🟨 JavaScript Tools":
        tabs = ["📷 Photo Capture & Email", "📸 Simple Photo Capture", "📧 Send to Gmail", 
                "🗺️ Current Location Map", "🛣️ Route Finder", "💬 WhatsApp Messenger"]
    else:  # Linux
        tabs = ["🐧 Linux Operations"]
    
    selected_tab = st.sidebar.radio("Select Tool:", tabs)
    
    # Main content area - simplified for initial run
    if selected_tab == "🔔 Notifications":
        show_notifications_page()
    elif selected_tab == "🌐 Web Scraper":
        show_web_scraper_page()
    elif selected_tab == "🔍 Google Search":
        show_google_search_page()
    elif selected_tab == "📧 Email Sender":
        show_email_sender_page()
    elif selected_tab == "🎨 Image Generator":
        show_image_generator_page()
    elif selected_tab == "🔄 Face Swap":
        show_face_swap_page()
    elif selected_tab == "💬 WhatsApp":
        show_whatsapp_page()
    elif selected_tab == "📱 SMS Sender":
        show_sms_sender_page()
    elif selected_tab == "📞 Phone Caller":
        show_phone_caller_page()
    elif selected_tab == "🖥 RAM Monitor":
        show_ram_monitor_page()
    elif selected_tab == "📲 WhatsApp Anonymous":
        show_whatsapp_anonymous_page()
    elif selected_tab == "📚 Tuple vs List":
        show_tuple_vs_list_page()
    elif selected_tab == "📷 Photo Capture & Email":
        show_photo_capture_page()
    elif selected_tab == "📸 Simple Photo Capture":
        show_simple_photo_capture_page()
    elif selected_tab == "📧 Send to Gmail":
        show_send_to_gmail_page()
    elif selected_tab == "🗺️ Current Location Map":
        show_current_location_page()
    elif selected_tab == "🛣️ Route Finder":
        show_route_finder_page()
    elif selected_tab == "💬 WhatsApp Messenger":
        show_whatsapp_messenger_page()
    elif selected_tab == "🐧 Linux Operations":
        show_linux_page()

def show_notifications_page():
    st.header("🔔 Notification Options")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📱 SMS Only"):
            st.success("SMS notification system activated!")
            
        if st.button("📞 Voice Call"):
            st.success("Voice call system activated!")
            
        if st.button("📱📞 SMS + Voice Call"):
            st.success("Combined SMS and Voice call system activated!")
            
        if st.button("🚀 All Channels"):
            st.success("All notification channels activated!")
    
    with col2:
        if st.button("💬 WhatsApp Only"):
            st.success("WhatsApp notification system activated!")
            
        if st.button("📱💬 SMS + WhatsApp"):
            st.success("Combined SMS and WhatsApp system activated!")
            
        if st.button("💬📞 WhatsApp + Voice Call"):
            st.success("Combined WhatsApp and Voice call system activated!")

def show_web_scraper_page():
    st.header("🌐 Website Data Downloader")
    st.write("Go on a website and download the entire data using Python")
    
    st.info("📋 Required libraries: requests, beautifulsoup4")
    st.code("pip install requests beautifulsoup4")
    
    url_input = st.text_input("Enter the website URL to scrape and download files from:")
    
    file_types = st.multiselect(
        "Select file types to download:",
        options=[".csv", ".txt", ".xlsx", ".xls", ".pdf", ".zip", ".jpg", ".png"],
        default=[".csv", ".xlsx"]
    )
    
    if st.button("Download Files"):
        if not url_input:
            st.error("Please enter a valid URL.")
        elif not file_types:
            st.error("Please select at least one file type to download.")
        else:
            st.info("Feature requires additional libraries. Install dependencies first.")

def show_google_search_page():
    st.header("🔍 Google Search")
    st.markdown("Enter a query below to search Google and get the top results.")
    
    st.info("📋 Required library: googlesearch-python")
    st.code("pip install googlesearch-python")
    
    with st.form("search_form"):
        query = st.text_input("Search Query", placeholder="e.g., Best places to visit in Rajasthan")
        num_results = st.slider("Number of results", min_value=5, max_value=25, value=10)
        submitted = st.form_submit_button("Search")
    
    if submitted:
        if not query:
            st.warning("Please enter a search query to begin.")
        else:
            st.info("Feature requires googlesearch-python library. Install dependencies first.")

def show_email_sender_page():
    st.header("📧 Email Sender")
    st.write("Send email using Python with Gmail SMTP")
    
    with st.expander("ℹ How to get Gmail App Password"):
        st.markdown("""
        1. Go to your Google Account settings
        2. Enable 2-Factor Authentication
        3. Go to Security → App passwords
        4. Generate an app password for this application
        5. Use the generated 16-character password below
        """)
    
    with st.form("email_form"):
        col1, col2 = st.columns(2)
        with col1:
            sender = st.text_input("Sender Email (Gmail)", placeholder="your-email@gmail.com")
            receiver = st.text_input("Receiver Email", placeholder="recipient@example.com")
        with col2:
            app_password = st.text_input("Gmail App Password", type="password")
            subject = st.text_input("Subject", placeholder="Email subject")
        
        message = st.text_area("Message", placeholder="Type your email message here...")
        anonymous_mode = st.checkbox("Send anonymously")
        
        submitted = st.form_submit_button("📤 Send Email")

        if submitted:
            if not sender or not app_password or not receiver or not message:
                st.error("All fields are required!")
            else:
                st.info("Email functionality ready - uses built-in Python libraries!")

def show_image_generator_page():
    st.header("🎨 Image Generator")
    st.write("Draw simple shapes and generate an image!")
    
    st.info("📋 Required library: Pillow")
    st.code("pip install Pillow")
    
    col1, col2 = st.columns(2)
    with col1:
        width = st.slider("Image width", 100, 800, 400)
        height = st.slider("Image height", 100, 800, 400)
    with col2:
        bg_color = st.color_picker("Background color", "#FFFFFF")
    
    shape = st.selectbox("Shape to draw", ["Circle", "Rectangle", "Line"])
    
    st.info("Install Pillow library to enable image generation functionality.")

def show_face_swap_page():
    st.header("🔄 Face Swap App")
    st.write("Swap faces in two images using AI")
    
    st.info("📋 Required libraries: opencv-python, mediapipe, numpy")
    st.code("pip install opencv-python mediapipe numpy")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("First Face Image")
        st.file_uploader("Upload first face image", type=["jpg", "jpeg", "png"], key="face1")
    with col2:
        st.subheader("Second Face Image")
        st.file_uploader("Upload second face image", type=["jpg", "jpeg", "png"], key="face2")
    
    st.info("Install required libraries to enable face swap functionality.")

def show_whatsapp_page():
    st.header("📱 WhatsApp Message Sender")
    st.write("Send WhatsApp messages using Python automation")
    
    st.info("📋 Required library: pywhatkit")
    st.code("pip install pywhatkit")
    
    phone = st.text_input("📞 Phone Number (with country code)", value="+91")
    message = st.text_area("💬 Enter Message", placeholder="Type your WhatsApp message here...")
    
    if st.button("📤 Send Message"):
        st.info("Install pywhatkit library to enable WhatsApp messaging.")

def show_sms_sender_page():
    st.header("📱 SMS Sender")
    st.write("Send SMS using Python")
    
    st.info("📋 Required library: twilio")
    st.code("pip install twilio")
    
    account_sid = st.text_input("Twilio SID")
    auth_token = st.text_input("Auth Token", type="password")
    from_number = st.text_input("Twilio Phone Number")
    to_number = st.text_input("Recipient Number")
    sms_body = st.text_area("SMS Body")
    
    if st.button("📤 Send SMS"):
        st.info("Install Twilio library and set up account to enable SMS functionality.")

def show_phone_caller_page():
    st.header("📞 Phone Caller")
    st.write("Make phone calls using Twilio")
    
    st.info("📋 Required library: twilio")
    st.code("pip install twilio")
    
    st.text_input("Twilio Account SID")
    st.text_input("Twilio Auth Token", type="password")
    st.text_input("Your Twilio Phone Number")
    st.text_input("Recipient's Phone Number")
    st.text_area("Message to Speak")
    
    if st.button("📞 Call Now"):
        st.info("Install Twilio library and set up account to enable calling functionality.")

def show_ram_monitor_page():
    st.header("🖥 RAM Monitor")
    st.write("Monitor system RAM usage")
    
    try:
        import psutil
        
        memory = psutil.virtual_memory()
        total_gb = memory.total / (1024 ** 3)
        used_gb = memory.used / (1024 ** 3)
        available_gb = memory.available / (1024 ** 3)
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Total RAM", f"{total_gb:.2f} GB")
        col2.metric("Used RAM", f"{used_gb:.2f} GB", f"{memory.percent}%")
        col3.metric("Available RAM", f"{available_gb:.2f} GB")
        
        st.progress(memory.percent / 100)
        
        if st.button("🔄 Refresh Data"):
            st.rerun()
            
    except ImportError:
        st.info("📋 Required library: psutil")
        st.code("pip install psutil")

def show_whatsapp_anonymous_page():
    st.header("📲 WhatsApp via Twilio")
    st.write("Send WhatsApp messages using Twilio API")
    
    st.info("📋 Required library: twilio")
    st.code("pip install twilio")
    
    st.text_input("Twilio Account SID")
    st.text_input("Twilio Auth Token", type="password")
    st.text_input("Recipient WhatsApp Number")
    st.text_area("Message to Send")
    
    if st.button("📤 Send WhatsApp Message"):
        st.info("Install Twilio library and set up WhatsApp API to enable this functionality.")

def show_tuple_vs_list_page():
    st.header("📚 Tuple vs List in Python")
    st.write("Technical comparison between Python's tuple and list types")
    
    data = [
        ["Mutability", "Mutable (can change)", "Immutable (cannot change)"],
        ["Syntax", "Square brackets: [ ]", "Parentheses: ( )"],
        ["Methods", "Many methods (append, remove, etc.)", "Few methods (count, index)"],
        ["Performance", "Slightly slower", "Faster"],
        ["Memory Usage", "More memory", "Less memory"],
        ["Hashability", "Not hashable", "Hashable"],
        ["Use Case", "Dynamic data", "Fixed data"],
    ]
    
    st.table({
        "Property": [row[0] for row in data],
        "List": [row[1] for row in data],
        "Tuple": [row[2] for row in data],
    })
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**List Example:**")
        st.code("""
my_list = [1, 2, 3]
my_list.append(4)
my_list[0] = 10
print(my_list)  # [10, 2, 3, 4]
        """, language="python")
    
    with col2:
        st.markdown("**Tuple Example:**")
        st.code("""
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # Error!
count = my_tuple.count(2)
index = my_tuple.index(3)
        """, language="python")

def show_photo_capture_page():
    st.header("📷 Photo Capture & Email")
    st.write("Capture photos using your camera and send them via email using JavaScript")
    
    # Setup instructions
    with st.expander("📋 Setup Instructions"):
        st.markdown("""
        **Required Setup for Email Functionality:**
        1. Create an account at [EmailJS](https://www.emailjs.com/)
        2. Get your Public Key from EmailJS dashboard
        3. Create an email service and template
        4. Replace the placeholder values in the code below
        
        **What this tool does:**
        - Access your device camera
        - Capture photos directly in the browser
        - Send captured photos via email using EmailJS
        """)
    
    # Configuration inputs
    st.subheader("🔧 EmailJS Configuration")
    col1, col2 = st.columns(2)
    
    with col1:
        public_key = st.text_input("EmailJS Public Key", placeholder="YOUR_PUBLIC_KEY")
        service_id = st.text_input("EmailJS Service ID", placeholder="YOUR_SERVICE_ID")
    
    with col2:
        template_id = st.text_input("EmailJS Template ID", placeholder="YOUR_TEMPLATE_ID")
        recipient_email = st.text_input("Default Recipient Email", placeholder="recipient@example.com")
    
    # Generate the HTML with user's configuration
    html_code = f"""
    <html>
    <head>
      <title>Click Photo & Send via Email</title>
      <script src="https://cdn.emailjs.com/dist/email.min.js"></script>
      <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }}
        .container {{
            background: rgba(255, 255, 255, 0.1);
            padding: 30px;
            border-radius: 15px;
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        }}
        video, img {{
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
        }}
        button {{
            background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 25px;
            cursor: pointer;
            font-size: 16px;
            margin: 10px;
            transition: transform 0.2s;
        }}
        button:hover {{
            transform: translateY(-2px);
        }}
        input {{
            padding: 12px;
            border-radius: 10px;
            border: none;
            margin: 10px;
            font-size: 16px;
            width: 300px;
        }}
        h2 {{
            text-align: center;
            margin-bottom: 30px;
        }}
      </style>
      <script>
        window.onload = () => {{
          emailjs.init("{public_key or 'YOUR_PUBLIC_KEY'}");
        }};

        function startCamera() {{
          navigator.mediaDevices.getUserMedia({{ video: true }})
            .then(stream => {{
              document.getElementById("video").srcObject = stream;
            }})
            .catch(err => {{
              alert("Camera access denied or not available: " + err.message);
            }});
        }}

        function capturePhoto() {{
          const video = document.getElementById("video");
          const canvas = document.getElementById("canvas");
          const ctx = canvas.getContext("2d");
          ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
          const imageData = canvas.toDataURL("image/png");
          document.getElementById("photo").src = imageData;
          document.getElementById("photo").style.display = "block";
          document.getElementById("emailSection").style.display = "block";
        }}

        function sendEmail() {{
          const imageData = document.getElementById("photo").src;
          const toEmail = document.getElementById("email").value || "{recipient_email or 'recipient@example.com'}";

          if (!toEmail.includes('@')) {{
            alert("Please enter a valid email address");
            return;
          }}

          const templateParams = {{
            to_email: toEmail,
            image_base64: imageData,
            from_name: "Photo Capture Tool",
            message: "Here's your captured photo!"
          }};

          emailjs.send("{service_id or 'YOUR_SERVICE_ID'}", "{template_id or 'YOUR_TEMPLATE_ID'}", templateParams)
            .then(() => {{
              alert("📧 Email sent successfully!");
            }})
            .catch((err) => {{
              alert("❌ Failed to send email: " + err.text);
              console.error("EmailJS Error:", err);
            }});
        }}
      </script>
    </head>
    <body onload="startCamera()">
      <div class="container">
        <h2>📷 Click Photo & Send via Email</h2>
        
        <div style="text-align: center;">
          <video id="video" width="400" height="300" autoplay></video><br><br>
          <button onclick="capturePhoto()">📷 Capture Photo</button><br><br>

          <canvas id="canvas" width="400" height="300" style="display:none;"></canvas>
          <img id="photo" width="400" style="display:none;" /><br><br>

          <div id="emailSection" style="display:none;">
            <input type="email" id="email" placeholder="Enter recipient email" value="{recipient_email or ''}" /><br><br>
            <button onclick="sendEmail()">📩 Send Photo via Email</button>
          </div>
        </div>
      </div>
    </body>
    </html>
    """
    
    # Display the interactive HTML
    if public_key and service_id and template_id:
        st.success("✅ Configuration complete! The photo capture tool is ready to use.")
        st.components.v1.html(html_code, height=800, scrolling=True)
    else:
        st.warning("⚠️ Please configure your EmailJS credentials above to use the photo capture tool.")
        st.info("💡 You can still preview the interface, but email functionality requires EmailJS setup.")
        
        # Show preview with placeholder values
        preview_html = html_code.replace('YOUR_PUBLIC_KEY', 'DEMO_MODE').replace('YOUR_SERVICE_ID', 'DEMO').replace('YOUR_TEMPLATE_ID', 'DEMO')
        st.components.v1.html(preview_html, height=800, scrolling=True)
    
    # Code display
    with st.expander("📝 View/Copy HTML Code"):
        st.code(html_code, language="html")
        st.download_button(
            label="📥 Download HTML File",
            data=html_code,
            file_name="photo_capture_email.html",
            mime="text/html"
        )

def show_simple_photo_capture_page():
    st.header("📸 Simple Photo Capture")
    st.write("Capture photos using your device camera with a simple interface")
    
    html_code = """
    <html>
    <head>
      <title>Simple Photo Capture</title>
      <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            background: linear-gradient(135deg, #74b9ff 0%, #0984e3 100%);
            color: white;
            text-align: center;
        }
        .container {
            background: rgba(255, 255, 255, 0.1);
            padding: 30px;
            border-radius: 15px;
            backdrop-filter: blur(10px);
        }
        video, img {
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
            margin: 10px;
        }
        button {
            background: linear-gradient(45deg, #00b894, #00cec9);
            color: white;
            border: none;
            padding: 15px 30px;
            border-radius: 25px;
            cursor: pointer;
            font-size: 16px;
            margin: 10px;
            transition: transform 0.2s;
        }
        button:hover {
            transform: translateY(-2px);
        }
      </style>
    </head>
    <body>
      <div class="container">
        <h2>📸 Simple Photo Capture</h2>
        <video id="video" width="400" height="300" autoplay></video><br>
        <button onclick="takePhoto()">📷 Take Photo</button><br><br>
        <canvas id="canvas" width="400" height="300" style="display:none;"></canvas>
        <img id="photo" width="400" style="display:none;"><br><br>
        <div id="photoTaken" style="display:none;">
          <p>✅ Photo captured successfully!</p>
          <button onclick="downloadPhoto()">💾 Download Photo</button>
        </div>
      </div>

      <script>
        // Camera setup
        navigator.mediaDevices.getUserMedia({ video: true })
          .then(stream => {
            document.getElementById('video').srcObject = stream;
          })
          .catch(err => {
            alert('Camera access denied: ' + err.message);
          });

        function takePhoto() {
          let canvas = document.getElementById('canvas');
          let video = document.getElementById('video');
          canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
          let photoURL = canvas.toDataURL();
          document.getElementById('photo').src = photoURL;
          document.getElementById('photo').style.display = 'block';
          document.getElementById('photoTaken').style.display = 'block';
          localStorage.setItem("photoURL", photoURL);
        }

        function downloadPhoto() {
          let canvas = document.getElementById('canvas');
          let link = document.createElement('a');
          link.download = 'captured-photo.png';
          link.href = canvas.toDataURL();
          link.click();
        }
      </script>
    </body>
    </html>
    """
    
    st.components.v1.html(html_code, height=700)
    
    with st.expander("📝 View/Copy HTML Code"):
        st.code(html_code, language="html")
        st.download_button(
            label="📥 Download HTML File",
            data=html_code,
            file_name="simple_photo_capture.html",
            mime="text/html"
        )

def show_send_to_gmail_page():
    st.header("📧 Send to Gmail")
    st.write("Send messages and content to Gmail using JavaScript")
    
    col1, col2 = st.columns(2)
    with col1:
        subject = st.text_input("Email Subject", value="Photo from my app")
        recipient = st.text_input("Recipient Email (optional)", placeholder="recipient@gmail.com")
    with col2:
        message = st.text_area("Email Message", value="Hello! I'm sending you this message from my web app.")
    
    html_code = f""
    <html>
    <head>
      <title>Send to Gmail</title>
      <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            background: linear-gradient(135deg, #fd79a8 0%, #e84393 100%);
            color: white;
            text-align: center;
        }}
        .container {{
            background: rgba(255, 255, 255, 0.1);
            padding: 30px;
            border-radius: 15px;
            backdrop-filter: blur(10px);
        }}
        button {{
            background: linear-gradient(45deg, #e17055, #d63031);
            color: white;
            border: none;
            padding: 15px 30px;
            border-radius: 25px;
            cursor: pointer;
            font-size: 16px;
            margin: 10px;
            transition: transform 0.2s;
        }}
        button:hover {{
            transform: translateY(-2px);
        }}
        input, textarea {{
            padding: 10px;
            border-radius: 10px;
            border: none;
            margin: 5px;
            width: 90%;
            font-size: 14px;
        }}
      </style>
    </head>
    <body>
      <div class="container">
        <h2>📧 Send to Gmail</h2>
        <input type="text" id="subject" value="{subject}" placeholder="Subject"><br>
        <input type="email" id="recipient" value="{recipient}" placeholder="Recipient (optional)"><br>
        <textarea id="message" rows="4" placeholder="Your message">{message}</textarea><br><br>
        <button onclick="sendToGmail()">📧 Open Gmail Composer</button>
        <button onclick="sendWithPhoto()">📧 Send with Photo</button>
      </div>

      <script>
        function sendToGmail() {{
          let subject = document.getElementById('subject').value || 'Message from Web App';
          let recipient = document.getElementById('recipient').value;
          let body = document.getElementById('message').value || 'Hello from my web application!';
          
          let mailtoLink = `mailto:${{recipient}}?subject=${{encodeURIComponent(subject)}}&body=${{encodeURIComponent(body)}}`;
          window.open(mailtoLink);
        }}

        function sendWithPhoto() {{
          let subject = document.getElementById('subject').value || 'Photo from Web App';
          let recipient = document.getElementById('recipient').value;
          let body = document.getElementById('message').value + '\n\n[Photo will be attached manually from your device]';
          
          let mailtoLink = `mailto:${{recipient}}?subject=${{encodeURIComponent(subject)}}&body=${{encodeURIComponent(body)}}`;
          window.open(mailtoLink);
        }}
      </script