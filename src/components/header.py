import streamlit as st


def header_home():

    logo_url = "https://i.ibb.co/HLRt0Cy4/Logo-Smart-Attend.png"
    
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px">
            <img src='{logo_url}' style='height:150px;' />
            <h1 style='text-align:center; color:#E0E3FF'>ATTEND SMART</h1>
        </div>   
                
                """, unsafe_allow_html=True)


def header_dashboard():

    logo_url = "https://i.ibb.co/HLRt0Cy4/Logo-Smart-Attend.png"
    
    st.markdown(f"""
        <div style="display:flex;align-items:center;justify-content:center;gap:12px;">
            <img src="{logo_url}" style="height:90px;display:block;align-self:center;"/>
            <h2 style="margin:0;color:#5865F2;font-weight:600;font-size:34px;line-height:1;">ATTEND SMART</h2>
        </div>
                
                """, unsafe_allow_html=True)