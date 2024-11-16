<template>
    <div class="login-bg">
        <div class="login-container">
            <div class="login-header">
                <div class="login-title">SkyShelf</div>
            </div>
            <el-form :model="param" :rules="rules" ref="login" size="large">
                <el-form-item prop="email">
                    <el-input v-model="param.email" placeholder="Email">
                        <template #prepend>
                            <el-icon>
                                <Message />
                            </el-icon>
                        </template>
                    </el-input>
                </el-form-item>
                <el-form-item prop="password">
                    <el-input
                        type="password"
                        placeholder="Password"
                        v-model="param.password"
                        show-password
                        @keyup.enter="submitForm(login)"
                    >
                        <template #prepend>
                            <el-icon>
                                <Lock />
                            </el-icon>
                        </template>
                    </el-input>
                </el-form-item>
                <!-- <div class="pwd-tips">
                    <el-checkbox class="pwd-checkbox" v-model="checked" label="Remember password" />
                    <el-link type="primary" @click="$router.push('/reset-pwd')">Forgot </el-link>
                </div> -->
                <el-button class="login-btn" type="primary" size="large" @click="submitForm(login)">Login</el-button>
                <p class="login-tips">Tips : rules to be declared</p>
                <p class="login-text">
                    No account?--<el-link type="primary" @click="$router.push('/register')">Sign Up</el-link>
                </p>
            </el-form>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue';
import { useRouter } from 'vue-router';
import { ElMessage } from 'element-plus';
import type { FormInstance, FormRules } from 'element-plus';

interface LoginInfo {
    email: string;
    password: string;
}

const lgStr = localStorage.getItem('login-param');
const defParam = lgStr ? JSON.parse(lgStr) : null;
const checked = ref(lgStr ? true : false);

const router = useRouter();
const param = reactive<LoginInfo>({
    email: defParam ? defParam.email : '',
    password: defParam ? defParam.password : '',
});

const rules: FormRules = {
    email: [
        {
            required: true,
            message: 'please enter email',
            trigger: 'blur',
        },
    ],
    password: [{ required: true, message: 'enter password', trigger: 'blur' }],
};
const login = ref<FormInstance>();
const submitForm = (formEl: FormInstance | undefined) => {
    if (!formEl) return;
    formEl.validate((valid: boolean) => {
        if (valid) {
            ElMessage.success('login successful');
            localStorage.setItem('vuems_token', "JWT_TOKEN");
            localStorage.setItem('vuems_name', param.email);
            router.push('/');
            if (checked.value) {
                localStorage.setItem('login-param', JSON.stringify(param));
            } else {
                localStorage.removeItem('login-param');
            }
        } else {
            ElMessage.error('login failed');
            return false;
        }
    });
};

</script>

<style scoped>
.login-bg {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 100vh;
    background: url(../../assets/img/login-bg.jpg) center/cover no-repeat;
}

.login-header {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 40px;
}

.logo {
    width: 35px;
}

.login-title {
    font-size: 22px;
    color: #333;
    font-weight: bold;
}

.login-container {
    width: 450px;
    border-radius: 5px;
    background: #fff;
    padding: 40px 50px 50px;
    box-sizing: border-box;
}

.pwd-tips {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 14px;
    margin: -10px 0 10px;
    color: #787878;
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
    color: #999;
}

.login-text {
    display: flex;
    align-items: center;
    margin-top: 20px;
    font-size: 14px;
    color: #787878;
}
</style>
