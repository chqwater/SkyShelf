<template>
  <div class="content-box-reco">
    <!-- <div class="search-bar">
      <ElInput
        style="width: 100%;"
        size="large"
        placeholder="Search book here"
        :suffix-icon="Search"
        v-model="searchTxt"
      ></ElInput>
    </div> -->
    <div class="recomm-card" v-for="category in param.recommendations" :key="category">
      <p style="color: white; font-size: 20px; font-weight: 500;">{{ category.name }}</p>
      <div class="card-bounder">
      <ElCarousel :interval="5000" type="card" height="600px">
        <ElCarouselItem v-for="item in category.books" :key="item" style="width: 400px;" @click="handleOpenBookOverview(category,item)">
          <img :src="item.img_url" style="width: 100%; height: 100%">
        </ElCarouselItem>
      </ElCarousel>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts" name="recommendation">
import { Search } from "@element-plus/icons-vue";
import { ElCarousel, ElCarouselItem, ElInput } from "element-plus";
import { onMounted, reactive, ref } from "vue";
import { useRouter } from "vue-router";
import { getRecommendation } from '../api/index';
import { ElLoading } from 'element-plus';

const router = useRouter();
const searchTxt = ref("");
const user_id: string | null = localStorage.getItem('vuems_id');
const param = reactive({
  recommendations: []
})

const loading = ElLoading.service({
    lock: true,
    text: 'Loading',
    background: 'rgba(0, 0, 0, 0.7)',
  })

const handleOpenBookOverview = (data1:any, data2:any)=>{
  console.log(data1,data2);
  router.push({
    path: '/home/overview',
    query: {
      category: data1.name,
      book_id: data2.id,
      title: data2.title,
      author: data2.author,
      description: data2.description,
      file_url: data2.file_url,
      img_url: data2.img_url
    }
  });
}

const loadRecommendation = async ()=>{
  await getRecommendation(user_id).then((res:any)=>{
    param.recommendations = res.recommendations;
  })
  loading.close();
}

onMounted(()=>{
  loadRecommendation();
})
</script>

<style scoped>
.content-box-reco {
  width: 100%;
  height: 100%;
  display: flex;
  position: relative;
  overflow-y: scroll;
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  scroll-snap-type: x mandatory;
}
.search-bar {
  min-width: 800px;
  height: 70px;
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  top: 80px;
  left: calc((100% - 600px) / 2);
  z-index: 9999;
}
.recomm-card{
  width: 900px;
  height: 660px;
  margin-top: 50px;
  margin-left: calc((100% - 900px)/2);
  background: linear-gradient(45deg, #409EFF, rgb(94, 69, 159));
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 20px 20px 5px 20px;
  border-radius: 50px;
  scroll-snap-align: center;
  scroll-snap-stop: always;
}
.recomm-card:not(:first-child) {
  margin-left: calc((100% - 900px) / 2);
}
.recomm-card:last-child {
  margin-right: calc((100% - 900px) / 2);
}
.recomm-card:hover{
  box-shadow: 0 0 90px rgba(64, 158, 255, 1.5), inset 0 0 15px rgba(94, 69, 159, 0.4); 
}
.card-bounder{
  width: 800px;
  height: 600px;
}
.el-carousel__item h3 {
  color: #475669;
  opacity: 0.75;
  line-height: 200px;
  margin: 0;
  text-align: center;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}
.el-carousel__item{
  border-radius: 50px;
  box-shadow: 10px 10px 20px rgba(0, 0, 0, 0.3);
}
</style>
