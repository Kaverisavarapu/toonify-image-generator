from pathlib import Path
import streamlit as st
import os
def load_css():

    css_file = (
        Path(__file__).parent
        / "styles.css"
    )

    with open(css_file) as f:

        st.markdown(
            f"""
            <style>
            {f.read()}
            </style>
            """,
            unsafe_allow_html=True
        )

load_css()
import streamlit as st
import requests
import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)
from services.auth_api import (
    login_user,
    signup_user
)

from services.image_api import (
    upload_image
)

from services.history_api import (
    get_history
)

from services.admin_api import (
    get_admin_stats
)
from services.profile_api import (
    get_profile,
    update_profile
)

from services.delete_api import (
    delete_history_item
)
from services.stats_api import (
    get_profile_stats
)
from services.payment_api import get_payments
from services.password_api import (
    change_password
)
from services.users_api import (
    get_all_users
)
from services.payment_api import (
    make_payment,
    get_payments,
    create_order,
    save_payment
)
import streamlit.components.v1 as components

import os

from dotenv import load_dotenv

load_dotenv()
st.error("APP.PY LOADED")
RAZORPAY_KEY = os.getenv(
    "RAZORPAY_KEY"
)
from effects import EFFECTS
st.set_page_config(
    page_title="Toonify",
    page_icon="🎨",
    layout="wide"
)

st.title("🎨 Toonify")
st.caption(
    "AI Powered Cartoon Generation Platform"
)

# ==================================================
# USER LOGGED IN
# ==================================================

if "user" in st.session_state:

    st.success(
        f"Welcome {st.session_state['user']['username']} 👋"
    )

    page = st.sidebar.radio(
    "Navigation",
    [
        "Upload",
        "Effects Store",
        "History",
        "Profile",
        "Payments",
        "Admin"
    ]
)
    # ==========================================
    # PROFILE
    # ==========================================

    st.subheader("Profile")

    st.write(
        f"Username: {st.session_state['user']['username']}"
    )

    st.write(
        f"Email: {st.session_state['user']['email']}"
    )




    st.divider()

    # ==========================================
    # UPLOAD PAGE
    # ==========================================

    if page == "Upload":

        st.subheader("🎨 Upload Image")

        uploaded_file = st.file_uploader(
            "Choose an image",
            type=["jpg", "jpeg", "png"]
        )

        if uploaded_file:

            st.image(
                uploaded_file,
                caption="Original Image",
                use_container_width=True
            )

            effect = st.selectbox(
                "🎨 Choose Effect",
                list(EFFECTS.keys())
            )

            price = EFFECTS[effect]["price"]

            if price == 0:

                st.success(
                    "This effect is FREE"
                )

            else:

                st.warning(
                    f"This effect costs ₹{price}"
                )

            if st.button(
                "Generate Cartoon"
            ):

                with st.spinner(
                    "Generating cartoon..."
                ):

                    result = upload_image(
                        st.session_state["user"]["id"],
                        uploaded_file,
                        effect
                    )

                    if result.get("success"):

                        st.json(result)

                        import os

                        filename = os.path.basename(
                            result["cartoon_image"]
                        )

                        image_url = (
                            f"https://toonify-image-generator-1.onrender.com/uploads/cartoons/{filename}"
                        )

                        st.write("Filename:", filename)
                        st.write("Image URL:", image_url)

                        st.session_state["generated"] = True
                        st.session_state["filename"] = filename
                        st.session_state["image_url"] = image_url
                        st.session_state["price"] = price
                        st.session_state["effect"] = effect

                        st.success(
                            "Cartoon generated successfully!"
                        )

                        st.rerun()

                    else:

                        st.error(
                            result.get(
                                "message",
                                "Generation failed"
                            )
                        )
        # ==========================================
        # SHOW GENERATED IMAGE
        # ==========================================

        if st.session_state.get("generated"):

            filename = st.session_state["filename"]
            image_url = st.session_state["image_url"]
            price = st.session_state["price"]
            effect = st.session_state["effect"]

            st.write("Stored URL:")
            st.write(image_url)

            response = requests.get(image_url)

            st.write("HTTP Status:", response.status_code)

            if response.status_code == 200:

                st.image(
                    image_url,
                    caption="Generated Cartoon",
                    use_container_width=True
                )

            else:

                st.error(
                    f"Image not found ({response.status_code})"
                )

            try:

                image_data = requests.get(
                    image_url
                ).content

                # FREE EFFECTS

                if price == 0:

                    st.download_button(
                        label="⬇ Download Cartoon",
                        data=image_data,
                        file_name=filename,
                        mime="image/png"
                    )

                # PAID EFFECTS

                else:

                    st.warning(
                        f"Pay ₹{price} to download"
                    )

                    if st.button(
                        f"💳 Pay ₹{price}"
                    ):

                        order = create_order(
                            price
                        )

                        order_id = order["id"]

                        st.success(
                            f"Order Created: {order_id}"
                        )

                        checkout_html = f"""
                                        <html>
                                        <head>
                                        <script src="https://checkout.razorpay.com/v1/checkout.js"></script>
                                        </head>

                                        <body>

                                        <script>

                                        var options = {{
                                            key: "{RAZORPAY_KEY}",
                                            amount: {price * 100},
                                            currency: "INR",
                                            name: "Toonify",
                                            description: "{effect}",
                                            order_id: "{order_id}",

                                            handler: function (response) {{
                                                alert("SUCCESS");
                                            }}
                                        }};

                                        var rzp = new Razorpay(options);

                                        window.onload = function() {{
                                            rzp.open();
                                        }};

                                        </script>

                                        </body>
                                        </html>
                                        """

                        components.html(
                                    checkout_html,
                                    height=700,
                                    scrolling=True
                                )
                        save_payment(
                            st.session_state["user"]["id"],
                            effect,
                            price,
                            order_id
                        )
                        st.session_state["payment_done"] = True
                        if st.session_state.get("payment_done"):

                            st.download_button(
                                label="⬇ Download Cartoon",
                                data=image_data,
                                file_name=filename,
                                mime="image/png"
                            )

            except Exception:

                st.warning(
                    "Download unavailable."
                )


            
    elif page == "Effects Store":

        from effects import EFFECTS

        st.header("🎨 Effects Store")

        for effect, details in EFFECTS.items():

            col1, col2 = st.columns([3,1])

            with col1:

                st.subheader(effect)

                st.write(
                    details["description"]
                )

            with col2:

                if details["price"] == 0:

                    st.success("FREE")

                else:

                    st.warning(
                        f"${details['price']}"
                    )

            st.divider()
    # ==========================================
    # HISTORY PAGE
    # ==========================================

    elif page == "History":

        st.subheader(
            "📂 Image History"
        )

        history = get_history(
            st.session_state["user"]["id"]
        )

        st.metric(
            "Total Cartoons",
            len(history)
        )

        if len(history) == 0:

            st.info(
                "No history found."
            )

        else:

            for item in history:

                st.divider()

                st.write(
    f"🎨 Effect: {item['effect_name']}"
)

                col1, col2 = st.columns(2)

                with col1:

                    original_file = os.path.basename(
                        item["original_image"]
                    )

                    original_url = (
                        f"https://toonify-image-generator-1.onrender.com/uploads/originals/{original_file}"
                    )

                    st.write("Original")

                    st.image(
                        original_url,
                        use_container_width=True
                    )


            with col2:

                generated_file = os.path.basename(
                    item["generated_image"]
                )

                generated_url = (
                    f"https://toonify-image-generator-1.onrender.com/uploads/cartoons/{generated_file}"
                )

                st.write("Generated Cartoon")

                st.image(
                    generated_url,
                    use_container_width=True
                )


            if st.button(
                f"Delete #{item['id']}"
            ):

                result = delete_history_item(
                    item["id"]
                )

                if result["success"]:

                    st.success(
                        "Deleted successfully"
                    )

                    st.rerun()

                else:

                    st.error(
                        "Failed to delete history."
                    )
    # ==========================================
    # ADMIN PAGE
    # ==========================================

    elif page == "Admin":

        st.subheader(
            "👨‍💼 Admin Dashboard"
        )

        stats = get_admin_stats()

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "👥 Total Users",
                stats["total_users"]
            )

        with col2:

            st.metric(
                "🖼 Total Images",
                stats["total_images"]
            )

        st.divider()

        if st.button("Logout"):

            st.session_state.clear()

            st.rerun()
        st.divider()

        st.subheader(
            "👥 Registered Users"
        )

        users = get_all_users()

        for user in users:

            st.write(
                f"ID: {user['id']} | "
                f"{user['username']} | "
                f"{user['email']} | "
                f"{user['role']}"
            )

    elif page == "Payments":

            st.header("💳 Payment History")
            payments = get_payments(
                st.session_state["user"]["id"]
            )


            if len(payments) == 0:

                st.info(
                    "No payments found."
                )

            else:

                for payment in payments:

                    st.divider()

                    st.write(
                        f"Effect: {payment['effect_name']}"
                    )

                    st.write(
                        f"Amount: ₹{payment['amount']}"
                    )

                    st.write(
                        f"Status: {payment['status']}"
                    )

                    st.write(
                        f"Date: {payment['created_at']}"
                    )
    elif page == "Profile":

        st.subheader(
            "👤 My Profile"
        )

        profile = get_profile(
            st.session_state["user"]["id"]
        )

        if profile["success"]:

            user = profile["user"]
            stats = get_profile_stats(
    user["id"]
)
            st.divider()

        st.subheader(
            "📊 Statistics"
        )

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Total Cartoons",
                stats["total_images"]
            )

        with col2:

       
            st.write(
                f"User ID: {user['id']}"
            )

            st.write(
                f"Email: {user['email']}"
            )

        

            st.divider()

            st.subheader(
                "Update Username"
            )

            new_username = st.text_input(
                "Username",
                value=user["username"]
            )

            if st.button(
                "Update Profile"
            ):

                result = update_profile(
                    user["id"],
                    new_username
                )

                if result["success"]:

                    st.success(
                        result["message"]
                    )

                    st.session_state["user"]["username"] = (
                        new_username
                    )

                    st.rerun()

                else:

                    st.error(
                        "Update failed"
                    )
            st.divider()

            st.subheader(
                "🔐 Security Settings"
            )

            old_password = st.text_input(
                "Old Password",
                type="password",
                key="old_password"
            )

            new_password = st.text_input(
                "New Password",
                type="password",
                key="new_password"
            )

            if st.button(
                "Change Password"
            ):

                result = change_password(
                    user["id"],
                    old_password,
                    new_password
                )

                if result["success"]:

                    st.success(
                        result["message"]
                    )

                else:

                    st.error(
                        result["message"]
                    )

    # elif page == "Premium":

    #     st.subheader(
    #         "💎 Premium Membership"
    #     )

    #     current_role = (
    #         st.session_state["user"]["role"]
    #     )

    #     st.write(
    #         f"Current Plan: {current_role}"
    #     )

    #     if current_role == "premium":

    #         st.success(
    #             "You already have Premium."
    #         )

    #     else:

    #         st.info(
    #             """
    #             Premium Features

    #             ✅ Unlimited Cartoon Generation
    #             ✅ Faster Processing
    #             ✅ HD Downloads
    #             ✅ Priority Support
    #             """
    #         )

    #         st.metric(
    #             "Price",
    #             "₹499"
    #         )

    #         if st.button(
    #             "Upgrade Now"
    #         ):

    #             result = upgrade_to_premium(
    #                 st.session_state["user"]["id"]
    #             )

    #             if result["success"]:

    #                 st.success(
    #                     "Premium Activated!"
    #                 )

    #                 st.session_state["user"]["role"] = (
    #                     "premium"
    #                 )

    #                 st.rerun()

    #             else:

    #                 st.error(
    #                     "Upgrade failed"
    #                 )

    
    # ==================================================
    # USER NOT LOGGED IN
    # ==================================================
else:

    menu = st.sidebar.selectbox(
        "Menu",
        [
            "Login",
            "Signup"
        ]
    )

    # ==========================================
    # SIGNUP
    # ==========================================

    if menu == "Signup":

        st.subheader(
            "Create Account"
        )

        username = st.text_input(
            "Username"
        )

        email = st.text_input(
            "Email"
        )

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Signup"):

            result = signup_user(
                username,
                email,
                password
            )

            if result["success"]:

                st.success(
                    result["message"]
                )

            else:

                st.error(
                    result["message"]
                )

    # ==========================================
    # LOGIN
    # ==========================================

    elif menu == "Login":

        st.subheader(
            "Login"
        )

        email = st.text_input(
            "Email"
        )

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login"):

            result = login_user(
                email,
                password
            )

            if result["success"]:

                st.session_state["token"] = (
                    result["access_token"]
                )

                st.session_state["user"] = (
                    result["user"]
                )

                st.rerun()

            else:

                st.error(
                    result["message"]
                )