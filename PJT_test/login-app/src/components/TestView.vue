<template>
  <section class="TestView">
    <div v-on:click="GoogleLoginBtn">구글 OAuth2 연동</div>
    <div id="my-signin2" style="display: none"></div>
    <button @click="Logout">logout</button>
  </section>
</template>

<script>

export default {
  name: "TestView",
  methods: {
    GoogleLoginBtn:function(){
      const self = this;

      window.gapi.signin2.render('my-signin2', {
        scope: 'profile email',
        width: 240,
        height: 50,
        longtitle: true,
        theme: 'dark',
        onsuccess: this.GoogleLoginSuccess,
        onfailure: this.GoogleLoginFailure,
      });

      setTimeout(function () {
        if (!self.googleLoginCheck) {
          const auth = window.gapi.auth2.getAuthInstance();
          auth.isSignedIn.get();
          document.querySelector('.abcRioButton').click();
        }
      }, 1500)

    },
    async GoogleLoginSuccess(googleUser) {
      const googleEmail = googleUser.getBasicProfile().getEmail();
      if (googleEmail !== 'undefined') {
        console.log(googleUser);
      }
    },
    //구글 로그인 콜백함수 (실패)
    GoogleLoginFailure(error) {
      console.log(error);
    },
    Logout(){
      const authInst = window.gapi.auth2.getAuthInstance();
      authInst.signOut().then(() => {
        // eslint-disable-next-line
        console.log('User Signed Out!!!');
      });
    }
  }
}
</script>

<style scoped>
  .test{ display:flex; justify-content: center; align-items: center; height:100vh; }
  div{ width: 200px; height:40px; background-color:#ffffff; border:1px #a8a8a8 solid; color:black; display:flex; align-items: center; justify-content: center; cursor:pointer; }
</style>