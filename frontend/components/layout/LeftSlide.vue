<template>
  <v-col cols="5" class="fill-height">
    <v-img
      src="/left_slide.png"
      max-height="100vh"
      cover
      class="align-end justify-center"
    >
      <v-row justify="center">
        <v-col md="8">
          <v-card height="220" class="transparent mb-16">
            <v-overlay :value="true" absolute color="#D2D1D1" opacity="0.8">
              <v-carousel
                v-model="slide"
                hide-delimiters
                :show-arrows="false"
                height="200"
                class="align-end rounded-xl"
              >
                <v-carousel-item v-for="(item, i) in items" :key="i">
                  <v-card dark flat class="transparent">
                    <p class="text-h6 px-4">“{{ item.comment }}”</p>

                    <v-card-text>
                      <v-row>
                        <v-col md="5">
                          <div class="text-h6">{{ item.name }}</div>
                        </v-col>
                        <v-col class="d-flex justify-end">
                          <v-rating
                            v-model="item.rating"
                            background-color="orange lighten-3"
                            color="orange"
                            dense
                          ></v-rating>
                        </v-col>
                      </v-row>
                      <v-row class="mt-0">
                        <v-col md="5">
                          <div class="text-caption">{{ item.education }}</div>
                        </v-col>
                        <v-col class="d-flex justify-end">
                          <v-btn icon outlined class="mr-3" @click="slide--">
                            <v-icon>mdi-arrow-left</v-icon>
                          </v-btn>
                          <v-btn icon outlined @click="slide++">
                            <v-icon>mdi-arrow-right</v-icon>
                          </v-btn>
                        </v-col>
                      </v-row>
                    </v-card-text>
                  </v-card>
                </v-carousel-item>
              </v-carousel>
            </v-overlay>
          </v-card>
        </v-col>
      </v-row>
    </v-img>
  </v-col>
</template>

<script>
export default {
  name: 'LeftSlide',
  data: () => ({
    items: [
      {
        comment:
          'Lorem ipsum dolor sit amet, consectetur adipiscing elit. ' +
          'A sit amet neque, id duis sed.',
        name: 'Ellen Rose',
        rating: 5,
        education: 'Harvard, Law 2nd Grade',
      },
      {
        comment:
          'Pharetra nibh eget vulputate interdum libero. ' +
          'A sit amet neque, id duis sed.',
        name: 'John Doe',
        rating: 4,
        education: 'John Hopkins, Medical 2nd Grade',
      },
      {
        comment:
          'Deneme test deneme test deneme. ' + 'A sit amet neque, id duis sed.',
        name: 'Jane Doe',
        rating: 3.5,
        education: 'John Hopkins, Medical 2nd Grade',
      },
    ],
    slide: 0,
    rating: 5,
  }),
}
</script>

<style scoped></style>
