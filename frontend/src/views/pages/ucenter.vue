<template>
  <div class="user-center-box">
    <p class="title">My Profile</p>
    <div class="user-box">
      <div class="header-a">
        <ElAvatar class="user-avator" :size="90" :icon="UserFilled"></ElAvatar>
        <p class="user-name">{{ username }}</p>
      </div>
      <p class="per-title">Personal Information</p>
      <div class="personal-info">
        <p>{{ username }}</p>
        <p>{{ email }}</p>
        <div class="journey">
          <p>My Journey: &nbsp;</p>
          <p>{{ prop.journeys }}&nbsp;</p>
          <div class="edit-btn">
            <ElButton type="primary" link :icon="Edit" @click="router.push('/journey')"
              >Edit</ElButton
            >
          </div>
        </div>
      </div>
      <div class="reading">
        <p>I'm Reading</p>
        <div class="book-list">
          <div class="book" v-for="item in prop.bookList">
            <img :src="item.img_url" style="width: 100%; height: 100%" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts" name="ucenter">
import { Edit, UserFilled } from "@element-plus/icons-vue";
import { ElAvatar, ElButton, ElIcon } from "element-plus";
import { useRouter } from "vue-router";
import { getShelf, getUserJourney } from "../../api";
import { onMounted, reactive } from "vue";

const username: string | null = localStorage.getItem("vuems_name");
const email: string | null = localStorage.getItem("vuems_email");
const user_id: string | null = localStorage.getItem("vuems_id");
const router = useRouter();
const prop = reactive({
  bookList: [],
  journeys: "",
});

const loadShelf = async () => {
  await getShelf(user_id).then((res: any) => {
    prop.bookList = res;
  });
};
const loadJourneys = async () => {
  await getUserJourney(user_id).then((res) => {
    prop.journeys = res.selected_journeys;
  });
};
onMounted(() => {
  loadShelf();
  loadJourneys();
});
</script>

<style scoped>
.user-center-box {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  width: 100%;
  font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS", sans-serif;
  flex-direction: column;
}
.user-box {
  background-color: white;
  height: 600px;
  width: 900px;
  border-radius: 40px;
  box-shadow: 0 0 10px 5px white;
}
.title {
  font-size: 25px;
  font-weight: 600;
}
.header-a {
  height: 120px;
  max-width: 100%;
  margin: 10px;
  padding: 10px;
  border-radius: 40px;
  border: 1px solid rgb(220, 220, 220);
  display: flex;
  flex-direction: row;
  align-items: center;
}
.user-avator {
  margin-left: 20px;
}
.user-name {
  margin-left: 40px;
  font-size: 30px;
}
.per-title {
  margin-left: 40px;
  font-size: 20px;
  margin-bottom: 0%;
}
.personal-info {
  height: 150px;
  max-width: 100%;
  margin: 0 10px 10px 10px;
  padding: 10px;
  border-radius: 40px;
  border: 1px solid rgb(220, 220, 220);
  display: flex;
  color: rgb(180, 180, 180);
  flex-direction: column;
  justify-content: center;
  padding-left: 40px;
}
.reading {
  height: 190px;
  max-width: 100%;
  margin: 0 10px 10px 10px;
  padding: 10px;
  border-radius: 40px;
  border: 1px solid rgb(220, 220, 220);
  display: flex;
  color: rgb(180, 180, 180);
  flex-direction: column;
}
.book-list {
  height: 160px;
  width: 100%;
  display: flex;
  flex-direction: row;
  margin-left: 20px;
  overflow: hidden;
  flex-wrap: nowrap;
}
.book {
  height: 140px;
  width: 90px;
  border-radius: 10px;
  border: 1px solid rgb(180, 180, 180);
  margin-right: 10px;
  overflow: hidden;
}
.journey {
  display: flex;
  flex-direction: row;
  align-items: center;
}
.edit-btn {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: end;
}
</style>
