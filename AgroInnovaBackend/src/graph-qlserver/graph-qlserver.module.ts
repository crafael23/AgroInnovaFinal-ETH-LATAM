import { Module } from '@nestjs/common';
import { ApolloDriver, ApolloDriverConfig } from '@nestjs/apollo';
import { GraphQLModule } from '@nestjs/graphql';
import { GraphQlserverResolver } from './graph-qlserver.resolver';
import { TypeormsqliteModule } from 'src/typeormsqlite/typeormsqlite.module';
import { GraphqlOptions } from './graphql.options';
import { MqttModule } from 'src/mqtt/mqtt.module';

@Module({
  imports: [
    GraphQLModule.forRootAsync<ApolloDriverConfig>({
      driver: ApolloDriver,
      useClass: GraphqlOptions,
    }),
    TypeormsqliteModule,
    MqttModule,
  ],
  controllers: [],
  providers: [GraphQlserverResolver],
})
export class GraphQlserverModule {}
