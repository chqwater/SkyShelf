<template>
  <div class="login-bg">
    <div class="login-container">
      <div class="login-header">
        <div class="login-title">SkyShelf</div>
      </div>
      <ElForm :model="param" :rules="rules" ref="login" size="large">
        <ElFormItem prop="email">
          <ElInput v-model="param.email" placeholder="Email">
            <template #prepend>
              <ElIcon>
                <Message />
              </ElIcon>
            </template>
          </ElInput>
        </ElFormItem>
        <ElFormItem prop="password">
          <ElInput
            type="password"
            placeholder="Password"
            v-model="param.password"
            show-password
            @keyup.enter="submitForm(login)"
          >
            <template #prepend>
              <ElIcon>
                <Lock />
              </ElIcon>
            </template>
          </ElInput>
        </ElFormItem>
        <!-- <div class="pwd-tips">
                    <el-checkbox class="pwd-checkbox" v-model="checked" label="Remember password" />
                    <el-link type="primary" @click="$router.push('/reset-pwd')">Forgot </el-link>
                </div> -->
        <ElButton class="login-btn" size="large" @click="submitForm(login)"
          >Login</ElButton
        >
        <p class="login-text">
          No account?&nbsp;&nbsp;<span
            class="navi-btn"
            @click="$router.push('/register')"
            style="color: white; text-decoration: underline"
            >Sign Up</span
          >
        </p>
      </ElForm>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted } from "vue";
import { useRouter } from "vue-router";
import { ElIcon, ElMessage, ElInput, ElButton, ElForm, ElFormItem } from "element-plus";
import type { FormInstance, FormRules } from "element-plus";
import { userLogin } from "../../api";
import { ElLoading } from "element-plus";

interface LoginInfo {
  email: string;
  password: string;
}

const lgStr = localStorage.getItem("login-param");
const defParam = lgStr ? JSON.parse(lgStr) : null;
const checked = ref(lgStr ? true : false);

const router = useRouter();
const param = reactive<LoginInfo>({
  email: defParam ? defParam.email : "",
  password: defParam ? defParam.password : "",
});

const rules: FormRules = {
  email: [
    {
      required: true,
      message: "please enter email",
      trigger: "blur",
    },
  ],
  password: [{ required: true, message: "enter password", trigger: "blur" }],
};
const login = ref<FormInstance>();
const submitForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return;
  const loading = ElLoading.service({
    lock: true,
    text: "Loading",
    background: "rgba(0, 0, 0, 0.7)",
  });
  formEl.validate(async (valid: boolean) => {
    if (valid) {
      await userLogin({
        email: param.email,
        password: param.password,
      }).then((res: any) => {
        localStorage.setItem("vuems_id", res.user_id);
        localStorage.setItem("vuems_token", "JWT_TOKEN");
        localStorage.setItem("vuems_name", res.username);
        localStorage.setItem("vuems_email", param.email);
        if (res.role === "admin") {
          localStorage.setItem("vuems_admin", "admin");
        }
        loading.close();
        router.push("/");
      });
    } else {
      ElMessage.error("login failed");
      return;
    }
  });
};
onMounted(() => {
  localStorage.removeItem("vuems_name");
  localStorage.removeItem("vuems_email");
  localStorage.removeItem("vuems_token");
  localStorage.removeItem("vuems_admin");
});
</script>

<style scoped>
.login-bg {
  display: flex;
  position: fixed;
  top: 0;
  left: 0;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100vh;
  background: url(../../assets/img/bg-bp.jpg) center/cover no-repeat;
}

.login-header {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 40px;
}
.login-bg::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(255, 255, 255, 0.6);
  z-index: 1;
}

.login-bg > * {
  position: relative;
  z-index: 2;
}

.logo {
  width: 35px;
}

.login-title {
  font-size: 30px;
  color: white;
  font-weight: bold;
  font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS", sans-serif;
}

.login-container {
  width: 380px;
  border-radius: 35px;
  background: linear-gradient(45deg, #409eff, rgb(94, 69, 159));
  padding: 40px 50px 50px;
}
.login-container:hover {
  width: 482px;
  box-sizing: border-box;
  border: 1px solid transparent;
  background-clip: padding-box;
  box-shadow: 0 0 90px rgba(64, 158, 255, 1.5), inset 0 0 15px rgba(94, 69, 159, 0.4);
}
.pwd-tips {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 14px;
  margin: -10px 0 10px;
  color: white;
}

.pwd-checkbox {
  height: auto;
}

.login-btn {
  display: block;
  width: 100%;
}

.login-tips {
  font-size: 12px;
  color: white;
  width: 100%;
  text-align: end;
  text-decoration: underline;
  cursor: pointer;
}

.login-text {
  margin-top: 20px;
  font-size: 14px;
  color: white;
  width: 100%;
  text-align: center;
}
.login-tips:hover {
  color: aqua !important;
}
:deep().el-input__wrapper {
  background-color: transparent;
  color: white;
  border: transparent;
  border-radius: 50px;
}
:deep().el-input__inner {
  color: white;
}
:deep().el-input-group__prepend {
  background-color: transparent;
  color: white;
  border-radius: 50px;
}
:deep().el-button {
  background-color: transparent;
  border-radius: 50px;
  font-size: 20px;
  color: white;
  display: flex;
  justify-content: center;
  font-weight: 600;
}
:deep().el-button:hover {
  color: aqua;
  box-shadow: 0 0 10px 5px white;
}
.navi-btn {
  cursor: pointer;
}
.navi-btn:hover {
  color: aqua !important;
}
</style>
